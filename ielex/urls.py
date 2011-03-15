from django.conf.urls.defaults import *
from ielex.views import *
from ielex import settings
from ielex.lexicon.views import *
from ielex.lexicon.models import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# additional arguments can be passed with a dictionary

# standard regexes for urls
R = {
    "COGJUDGE_ID":r"(?P<cogjudge_id>\d+)",
    "DOMAIN":r"(?P<domain>[a-zA-Z0-9_.-]+)",
    "LANGUAGE":r"(?P<language>[a-zA-Z0-9_-]+)",
    "LEXEME_ID":r"(?P<lexeme_id>\d+)",
    "MEANING":r"(?P<meaning>[a-zA-Z0-9_]+)",
    "RELATION":r"(?P<relation>[a-zA-Z0-9_.-]+)",
    "WORDLIST":r"(?P<wordlist>[a-zA-Z0-9_.-]+)",
    }

urlpatterns = patterns('',
    # Front Page
    url(r'^$', view_frontpage, name="view-frontpage"),
    url(r'^backup/$', make_backup),
    url(r'^changes/$', view_changes, name="view-changes"),
    # url(r'^touch/(?P<model_name>[a-zA-Z0-9_ ]+)/(?P<model_id>\d+)/', touch),

    # Languages
    url(r'^languages/$', view_language_list, name="view-languages"),
    url(r'^languages/reorder/$', language_reorder, name="language-reorder"),
    url(r'^languages/add-new/$', language_add_new, name="language-add-new"),
    url(r'^languages/sort/(?P<ordered_by>sort_key|utf8_name)/$', sort_languages,
            name="language-sort"),

    # Language
    url(r'^language/%(LANGUAGE)s/$' % R, language_report,
            name="language-report"),
    ## TODO Change this to
    # url(r'^language/%(LANGUAGE)s/lexemes/%(WORDLIST)s/$' % R, language_report,
    #         name="language-report"),
    url(r'^language/%(LANGUAGE)s/edit/$' % R, edit_language,
            name="language-edit"),
    url(r'^language/%(LANGUAGE)s/delete/$' % R, delete_language,
            name="language-delete"),
    url(r'^language/%(LANGUAGE)s/add-lexeme/' % R,
            lexeme_add, {"return_to":"/language/%(language)s/"}),
    url(r'^language/%(LANGUAGE)s/add-lexeme/%(MEANING)s/' % R,
            lexeme_add, {"return_to":"/language/%(language)s/"}),

    # Meanings (aka wordlist)
    url(r'^wordlist/%(WORDLIST)s/$' % R, view_wordlist, name="view-wordlist"),
    # url(r'^wordlist/%(WORDLIST)s/edit/$' % R, edit_wordlist,
    #         name="edit-wordlist"),
    #url(r'^wordlist/%(WORDLIST)s/reorder/$' % R, reorder_wordlist,
    #         name="reorder-wordlist"),
    url(r'^meanings/$', view_wordlist, {"wordlist":"all"}, name="view-meanings"),
    url(r'^meanings/add-new/$', meaning_add_new, name="meaning-add-new"),
    url(r'^meaning/%(MEANING)s/edit/$' % R, edit_meaning,
            name="meaning-edit"),

    # Meaning
    url(r'^meaning/%(MEANING)s/add-lexeme/$' % R, lexeme_add,
            {"return_to":"/meaning/%(meaning)s/"}),
    url(r'^meaning/%(MEANING)s/$' % R, report_meaning,
            name="meaning-report"),
    url(r'^meaning/%(MEANING)s/add/$' % R, report_meaning,
            name="meaning-add-lexeme"),
    url(r'^meaning/%(MEANING)s/%(LEXEME_ID)s/$' % R,
            report_meaning, {"action":"goto"}),
    url(r'^meaning/%(MEANING)s/%(LEXEME_ID)s/add/$' % R,
            report_meaning, {"action":"add"}),
    url(r'^meaning/%(MEANING)s/%(LEXEME_ID)s/%(COGJUDGE_ID)s/$' % R,
            report_meaning),
    url(r'^meaning/%(MEANING)s/add-lexeme/' % R,
            lexeme_add, {"return_to":"/meaning/%(meaning)s/"}),
    url(r'^meaning/%(MEANING)s/add-lexeme/%(LANGUAGE)s/' % R,
            lexeme_add, {"return_to":"/meaning/%(meaning)s/"}),

    # Lexemes
    url(r'^lexeme/add/', lexeme_add, {"return_to":"/meanings/"}),
    url(r'^lexeme/search/$', lexeme_search, name="lexeme-search"),

    url(r'^lexeme/%(LEXEME_ID)s/duplicate/$' % R, lexeme_duplicate),
    url(r'^lexeme/%(LEXEME_ID)s/$' % R,
            view_lexeme, name="view-lexeme"),
    url(r'^lexeme/%(LEXEME_ID)s/(?P<action>add-citation|edit|add-cognate|add-new-citation)/$' % R,
            lexeme_edit),
    url(r'^lexeme/%(LEXEME_ID)s/(?P<action>edit-citation|delink-citation)/(?P<citation_id>\d+)/$' % R,
            lexeme_edit),
    url(r'^lexeme/%(LEXEME_ID)s/(?P<action>delink-cognate)/%(COGJUDGE_ID)s/$' % R,
            lexeme_edit),
    url(r'^lexeme/%(LEXEME_ID)s/(?P<action>edit-cognate-citation)/(?P<citation_id>\d+)/$' % R,
            lexeme_edit), # just use <cogjudge_id>
    url(r'^lexeme/%(LEXEME_ID)s/(?P<action>delink-cognate-citation)/(?P<citation_id>\d+)/$' % R,
            lexeme_edit),
    url(r'^lexeme/%(LEXEME_ID)s/(?P<action>add-cognate-citation|add-new-cognate-citation)/%(COGJUDGE_ID)s/$' % R,
            lexeme_edit),
    url(r'^lexeme/%(LEXEME_ID)s/(?P<action>add-new-cognate)/$' % R, lexeme_edit),
    url(r'^lexeme/%(LEXEME_ID)s/(?P<action>delete)/$' % R, lexeme_edit),

    # Sources
    url(r'^sources/$', source_list, name="view-sources"),
    url(r'^source/(?P<source_id>\d+)/$', source_edit),
    url(r'^source/(?P<source_id>\d+)/(?P<action>edit|delete)/$', source_edit),
    url(r'^source/(?P<action>add)/$', source_edit),
    url(r'^source/(?P<action>add)/cognate-judgement/%(COGJUDGE_ID)s/$' % R, source_edit),
    url(r'^source/(?P<action>add)/lexeme/%(LEXEME_ID)s/$' % R, source_edit),

    # Cognates
    url(r'^cognate/(?P<cognate_id>\d+)/$', cognate_report, name="cognate-set"),
    url(r'^cognate/(?P<cognate_id>\d+)/(?P<action>edit)/$', cognate_report),
    url(r'^cognate/%(MEANING)s/(?P<code>[A-Z]+[0-9]*)/$' % R,
            cognate_report),

    url(r'^revert/(?P<version_id>\d+)/$', revert_version),
    url(r'^object-history/(?P<version_id>\d+)/$', view_object_history),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    )

urlpatterns += patterns('',
        ('', include('ielex.extensional_semantics.urls')),
        )

urlpatterns += patterns('',
        (r'^nexus/$', 'ielex.lexicon.views.list_nexus'),
        (r'^nexus-data/$', 'ielex.lexicon.views.write_nexus'),
        )

urlpatterns += patterns('django.contrib.auth',
    (r'^accounts/login/$','views.login', {'template_name':
        'profiles/login.html'}),
    (r'^accounts/logout/$','views.logout', {'template_name':
        'profiles/logout.html'}),
    )

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/profile/$', 'ielex.profiles.views.view_profile'),
    (r'^accounts/alter/profile/$', 'ielex.profiles.views.alter_profile'),
    (r'^accounts/change-password/$', 'ielex.profiles.views.change_password'),
    (r'^accounts/profile/(?P<username>.+)/$',
        'ielex.profiles.views.view_profile'),
    (r'^accounts/alter/profile/(?P<username>.+)/$',
        'ielex.profiles.views.alter_profile'),
    )

if settings.DEBUG: # additional urls for testing purposes
    urlpatterns += patterns('',
    # this is needed for running the development server
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
    )

# vim:nowrap
