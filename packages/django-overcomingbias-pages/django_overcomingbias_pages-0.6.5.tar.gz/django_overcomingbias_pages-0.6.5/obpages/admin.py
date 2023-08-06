from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.decorators import method_decorator
from django.utils.text import Truncator
from django.views.decorators.csrf import csrf_protect
from obapi.admin import OBContentItemAdmin
from obapi.models import OBContentItem
from ordered_model.admin import OrderedInlineModelAdminMixin, OrderedTabularInline

import obpages.tasks
from obpages.models import (
    CuratedContentItem,
    FeedbackNote,
    SearchIndex,
    User,
    UserSequence,
    UserSequenceMember,
)

admin.site.register(User, UserAdmin)


class SpamScoreListFilter(admin.SimpleListFilter):
    title = "spam score"
    parameter_name = "spam_score"

    def lookups(self, request, model_admin):
        return (
            ("gt80", ">0.8"),
            ("gt50", ">0.5"),
            ("le50", "<=0.5"),
            ("none", "No Score"),
        )

    def queryset(self, request, queryset):
        if self.value() == "gt80":
            return queryset.filter(spam_score__gt=0.8)
        if self.value() == "gt50":
            return queryset.filter(spam_score__gt=0.5)
        if self.value() == "lte50":
            return queryset.filter(spam_score__lte=0.5)
        if self.value() == "none":
            return queryset.filter(spam_score=None)


@admin.register(FeedbackNote)
class FeedbackNoteAdmin(admin.ModelAdmin):
    readonly_fields = ("create_timestamp",)
    list_display = (
        "__str__",
        "create_timestamp",
        "no_further_action",
        "spam_score",
        "truncated_text",
    )
    list_filter = (
        "no_further_action",
        SpamScoreListFilter,
        ("user", admin.EmptyFieldListFilter),
    )

    @admin.display(description="Text")
    def truncated_text(self, obj):
        return Truncator(obj.feedback).chars(num=50, truncate="...")


@admin.register(SearchIndex)
class SearchIndexAdmin(admin.ModelAdmin):
    manage_search_template = "admin/obpages/manage_search.html"

    def get_urls(self):
        return [
            path(
                "",
                self.admin_site.admin_view(self.manage_search_view),
                name="obpages_searchindex_changelist",
            )
        ]

    @method_decorator(csrf_protect)
    def manage_search_view(self, request):
        # (1) Check permissions
        if not self.has_module_permission(request):
            raise PermissionDenied

        # (2)
        opts = self.model._meta

        if request.method == "POST":
            # Configure action
            if "_update" in request.POST:
                required_permission = "obpages.update_search_index"
                searchindex_task = obpages.tasks.update_search_index
                success_message = "Updating search index. This may take a while..."
            elif "_rebuild" in request.POST:
                required_permission = "obpages.rebuild_search_index"
                searchindex_task = obpages.tasks.rebuild_search_index
                success_message = "Rebuilding search index. This may take a while..."
            else:
                raise SuspiciousOperation

            # Execute action
            if not request.user.has_perm(required_permission):
                raise PermissionDenied

            # Run task
            searchindex_task()
            self.message_user(request, message=success_message, level=messages.INFO)

        context = {
            **self.admin_site.each_context(request),
            "module_name": str(opts.verbose_name_plural),
            "title": "Search Index Management",
            "subtitle": None,
            "is_popup": False,
            "opts": opts,
        }

        request.current_app = self.admin_site.name

        # Prevent form resubmission if page is refreshed
        if request.method == "POST":
            return HttpResponseRedirect(request.get_full_path())

        return TemplateResponse(request, self.manage_search_template, context)


class UserSequenceMemberInline(OrderedTabularInline):
    model = UserSequenceMember
    fields = (
        "content_item",
        "order",
        "move_up_down_links",
    )
    readonly_fields = (
        "order",
        "move_up_down_links",
    )
    ordering = ("order",)
    extra = 1
    autocomplete_fields = ("content_item",)


@admin.register(UserSequence)
class UserSequenceAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    model = UserSequence
    list_display = ("title",)
    inlines = (UserSequenceMemberInline,)
    readonly_fields = ("create_timestamp", "update_timestamp")


@admin.register(CuratedContentItem)
class CuratedContentItemAdmin(admin.ModelAdmin):
    model = CuratedContentItem
    autocomplete_fields = ("content_item",)


# Override obapi content item admin
admin.site.unregister(OBContentItem)


@admin.register(OBContentItem)
class CustomOBContentItemAdmin(OBContentItemAdmin):
    """OBContentItemAdmin which uses Huey to pull and sync posts asynchronously."""

    def pull(self, request):
        # Dispatch task
        obpages.tasks.download_new_items()
        # Message user
        self.message_user(
            request=request,
            message="Downloading new posts. Please wait up to 30 minutes.",
            level=messages.INFO,
        )

    def sync(self, request):
        # Dispatch task
        obpages.tasks.update_edited_items(user_pk=request.user.pk)
        # Message user
        self.message_user(
            request=request,
            message="Updating existing posts. Please wait a few minutes.",
            level=messages.INFO,
        )
