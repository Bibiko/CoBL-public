from django.conf.urls.defaults import *
from ielex.views import *
from ielex import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Front Page
    url('^$', view_frontpage, name="view-frontpage"),

    # List of languages in the database
    url('^languages/$', view_languages, name="view-languages"),
    # Swadesh list for one language
    url(r'^language/([a-zA-Z0-9_ ]+)/$', report_language,
            name="language-report"), # usage {% url language-report English %}

    # List of meanings in the database
    url('^meanings/$', view_meanings, name="view-meanings"),
    # All forms in the database with a particular meaning
    url(r'^word/([a-zA-Z0-9_ ]+|\d+)/(edit/|add/)?$', report_word,
            name="word-report"),
    url(r'^word/([a-zA-Z0-9_ ]+|\d+)/(edit)/(\d+)/$', report_word,
            name="word-report"), # XXX

    url(r'^lexeme/(?P<lexeme_id>\d+)/(?P<action>add-citation|edit-lexeme|add-cognate)?$', report_lexeme, name="lexeme-report"),
    url(r'^lexeme/(?P<lexeme_id>\d+)/(?P<action>edit-citation)/(?P<citation_id>\d+)$', report_lexeme, name="lexeme-report"),
    # url(r'^lexeme/(?P<lexeme_id>\d+)/(?P<action>edit-judgement)/(?P<judgement_id>\d+)$', report_lexeme, name="lexeme-report"),
    url(r'^lexeme/(?P<lexeme_id>\d+)/(?P<action>edit-cognate)/(?P<cognate_class_id>\d+)/(?P<citation_id>\d+)$',
            report_lexeme, name="lexeme-report"),
    url(r'^lexeme/(?P<lexeme_id>\d+)/(?P<action>add-cognate-citation)/(?P<cognate_class_id>\d+)$', report_lexeme, name="lexeme-report"),
    url(r'^source/word/(\d+)/', word_source,
            name="word-source"),
    # url(r'/source/judgement/(\d+/)(edit/)?', lexeme_source, 
    #         name="lexeme-source"),

    # Example:
    # (r'^ielex/', include('ielex.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    )


if settings.DEBUG: # additional urls for testing purposes
    urlpatterns += patterns('',
    # this is needed for running the development server
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),

    (r'^test-form/$', test_form),
    (r'^test-form/new-word/$', test_form_newword),
    (r'^test-form/choose-source/$', test_form_choosesource),
    (r'^test-form/choose-language/$', test_form_chooselanguage),
    (r'^test-form/new-source/$', test_form_newsource),
    (r'^test-success/', test_success),

    )
