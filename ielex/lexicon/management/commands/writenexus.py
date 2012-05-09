from optparse import make_option
from os.path import expanduser, expandvars
from django.core.management.base import NoArgsCommand, CommandError
from ielex.lexicon.views import write_nexus
from ielex.lexicon.models import LanguageList, MeaningList

class Command(NoArgsCommand):
    help="""Export a nexus file from the database"""
    requires_model_validation = False
    unique_choices = ["all", "limited", "none"]
    # option_list = NoArgsCommand.option_list + (
    option_list = (
            make_option("--language-list", dest="language_list",
                action="store", default="all", metavar="NAME",
                help="Name of language list [%s]" % LanguageList.DEFAULT),
            make_option("--meaning-list", dest="meaning_list",
                action="store", default="all", metavar="NAME",
                help="Name of meaning list [%s]" % MeaningList.DEFAULT),
            make_option("--unique", dest="unique", metavar=("{%s}" %
                "|".join(unique_choices)),
                action="store", type="choice", default=unique_choices[0],
                choices=unique_choices ,
                help=("Include unique cognate sets [%s]" % unique_choices[0])),
            make_option("--suppress-invariant", dest="exclude_invariant",
                action="store_true", default=False,
                help="Suppress cognate sets with a reflex present"\
                " in all languages (missing data is not treated as"\
                " evidence of variation) [don't suppress]"),
            make_option("--outfile", dest="filename",
                action="store", default=None,
                help="Name of destinate filename [output to screen]"),
            )

    def run_from_argv(self, argv):
        """
        A version of the method from
        Django-1.3-py2.7.egg/django/core/management/base.py
        with call to `handle_default_options` disabled in order to
        suppress unwanted default options.
        """
        parser = self.create_parser(argv[0], argv[1])
        options, args = parser.parse_args(argv[2:])
        # handle_default_options(options)
        assert not hasattr(options, "settings")
        assert not hasattr(options, "pythonpath")
        self.execute(*args, **options.__dict__)
        return

    def handle(self, **options):
        if options["filename"]:
            fileobj = open(expanduser(expandvars(options["filename"])), "w")
        else:
            fileobj = self.stdout
        if options["unique"] == 'none':
            options["unique"] = False
        fileobj = write_nexus(fileobj,
            options["language_list"],
            options["meaning_list"],
            set(["L","X"]), # exclude
            "NN", # dialect
            True, # label cognate sets
            options["unique"],
            options["exclude_invariant"])
        fileobj.close()
        return

