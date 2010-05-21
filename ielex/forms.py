from django import forms
# from ielex.views import get_languages
from ielex.lexicon.models import *

class ChooseLanguageField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.utf8_name or obj.ascii_name

class ChooseLanguagesField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.utf8_name or obj.ascii_name

class ChooseLanguageListField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class ChooseMeaningListField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class ChooseMeaningField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.gloss

class ChooseCognateClassField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.alias

class ChooseSourcesField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        def truncate(s, l):
            if len(s) < l:
                return s
            else:
                return s[:l-4]+" ..."
        return truncate(obj.citation_text, 124)

class ChooseOneSourceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        def truncate(s, l):
            if len(s) < l:
                return s
            else:
                return s[:l-4]+" ..."
        return truncate(obj.citation_text, 124)

class AddLexemeForm(forms.Form):
    # Needs some custom validation: requires one of source_form and phon_form,
    # and will copy source_form to phon_form if empty
    # Need to think about the default sort order of the Language objects here
    # It might make sense to have it alphabetical
    language = ChooseLanguageField(queryset=Language.objects.all())
    meaning = ChooseMeaningField(queryset=Meaning.objects.all())
    source_form = forms.CharField(required=False)
    phon_form = forms.CharField(required=False)
    notes = forms.CharField(
            widget=forms.Textarea,
            label="Notes",
            required=False)

class EditLexemeForm(forms.Form):
    # needs some custom validation: requires one of source_form and phon_form,
    # and will copy source_form to phon_form if empty
    source_form = forms.CharField(required=False)
    phon_form = forms.CharField(required=False)
    notes = forms.CharField(
            widget=forms.Textarea,
            label="Notes",
            required=False)
    # sources = ChooseSourcesField(queryset=Source.objects.all())

class EditSourceForm(forms.ModelForm):
    type_code = forms.ChoiceField(choices=Source.TYPE_CHOICES,
            widget=forms.RadioSelect())
    class Meta:
        model = Source

class EditLanguageForm(forms.ModelForm):

    def clean_ascii_name(self):
        data = self.cleaned_data["ascii_name"]
        try: # ascii name must be ascii
            data.decode("ascii")
        except UnicodeEncodeError:
            raise forms.ValidationError("'%s' contains non-ASCII characters" %
                    data)
        try: # ascii name cannot have whitespace
            assert " " not in data
        except AssertionError:
            raise forms.ValidationError(
                    "ASCII name cannot contain whitespace (try '%s')" %
                    data.replace(" ","_"))
        # try:
        #     assert not Language.objects.filter(
        #             ascii_name=data).exclude(id=self.cleaned_data["id"])
        # except AssertionError:
        #     raise forms.ValidationError("This ASCII name is already in use")
        return data

    class Meta:
        model = Language

class ChooseLanguageForm(forms.Form):
    # Need to think about the default sort order of the Language objects here
    # It might make sense to have it alphabetical
    language = ChooseLanguageField(queryset=Language.objects.all(),
            widget=forms.Select(attrs={"onchange":"this.form.submit()"}))

class ChooseLanguageListForm(forms.Form):
    language_list = ChooseLanguageListField(
            queryset=LanguageList.objects.all(),
            empty_label=None,
            widget=forms.Select(attrs={"onchange":"this.form.submit()"}))

class ChooseMeaningListForm(forms.Form):
    meaning_list = ChooseMeaningListField(
            queryset=MeaningList.objects.all(),
            empty_label=None,
            widget=forms.Select(attrs={"onchange":"this.form.submit()"}))

class ChooseNexusOutputForm(forms.Form):
    language_list = ChooseLanguageListField(
            queryset=LanguageList.objects.all(),
            empty_label=None,
            widget=forms.Select())
    meaning_list = ChooseMeaningListField(
            queryset=MeaningList.objects.all(),
            empty_label=None,
            widget=forms.Select())
    reliability = forms.MultipleChoiceField(choices=Source.RELIABILITY_CHOICES,
            widget=forms.CheckboxSelectMultiple,
            label="Exclude ratings")
    unique = forms.BooleanField(label="Include unique states")

class ChooseSourceForm(forms.Form):
    source = ChooseSourcesField(queryset=Source.objects.all())

class EditCitationForm(forms.Form):
    pages = forms.CharField(required=False)
    reliability = forms.ChoiceField(choices=Source.RELIABILITY_CHOICES,
            widget=forms.RadioSelect)
    comment = forms.CharField(widget=forms.Textarea, required=False)

class AddCitationForm(forms.Form):
    source = ChooseOneSourceField(queryset=Source.objects.all())
    pages = forms.CharField(required=False)
    reliability = forms.ChoiceField(choices=Source.RELIABILITY_CHOICES,
            widget=forms.RadioSelect)
    comment = forms.CharField(widget=forms.Textarea, required=False)

class ChooseCognateClassForm(forms.Form):
    cognate_class = ChooseCognateClassField(queryset=CognateSet.objects.all(),
            widget=forms.Select(attrs={"onchange":"this.form.submit()"}),
            empty_label="---",
            label="")

class EditCognateSetForm(forms.Form):
    notes = forms.CharField(widget=forms.Textarea, required=False)

class ReorderLanguageSortKeyForm(forms.Form):
    language = ChooseLanguagesField(
            queryset=Language.objects.all().order_by("sort_key"),
            widget=forms.Select(attrs={"size":20}),
            empty_label=None)
