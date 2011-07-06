# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Rename table (added manually, replace create_table and delete_table
        # calls)
        db.rename_table('lexicon_cognateset', 'lexicon_cognateclass')

        # Changing field 'CognateJudgement.cognate_class'
        db.alter_column('lexicon_cognatejudgement', 'cognate_class_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lexicon.CognateClass']))

        # Changing field 'DyenCognateSet.cognate_class'
        db.alter_column('lexicon_dyencognateset', 'cognate_class_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lexicon.CognateClass']))

        # Changing field 'CognateClassCitation.cognate_class'
        db.alter_column('lexicon_cognateclasscitation', 'cognate_class_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lexicon.CognateClass']))

    def backwards(self, orm):

        # Rename table (added manually)
        db.rename_table('lexicon_cognateclass', 'lexicon_cognateset')

        # Changing field 'CognateJudgement.cognate_class'
        db.alter_column('lexicon_cognatejudgement', 'cognate_class_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lexicon.CognateSet']))

        # Changing field 'DyenCognateSet.cognate_class'
        db.alter_column('lexicon_dyencognateset', 'cognate_class_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lexicon.CognateSet']))

        # Changing field 'CognateClassCitation.cognate_class'
        db.alter_column('lexicon_cognateclasscitation', 'cognate_class_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lexicon.CognateSet']))

    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lexicon.cognateclass': {
            'Meta': {'ordering': "['alias']", 'object_name': 'CognateClass'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {})
        },
        'lexicon.cognateclasscitation': {
            'Meta': {'unique_together': "(('cognate_class', 'source'),)", 'object_name': 'CognateClassCitation'},
            'cognate_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lexicon.CognateClass']"}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '999'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '999'}),
            'reliability': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lexicon.Source']"})
        },
        'lexicon.cognatejudgement': {
            'Meta': {'object_name': 'CognateJudgement'},
            'cognate_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lexicon.CognateClass']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lexeme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lexicon.Lexeme']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lexicon.Source']", 'through': "orm['lexicon.CognateJudgementCitation']", 'symmetrical': 'False'})
        },
        'lexicon.cognatejudgementcitation': {
            'Meta': {'unique_together': "(('cognate_judgement', 'source'),)", 'object_name': 'CognateJudgementCitation'},
            'cognate_judgement': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lexicon.CognateJudgement']"}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '999'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '999'}),
            'reliability': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lexicon.Source']"})
        },
        'lexicon.dyencognateset': {
            'Meta': {'object_name': 'DyenCognateSet'},
            'cognate_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lexicon.CognateClass']"}),
            'doubtful': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'lexicon.dyenname': {
            'Meta': {'ordering': "['name']", 'object_name': 'DyenName'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lexicon.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '999'})
        },
        'lexicon.genericcitation': {
            'Meta': {'unique_together': "(('content_type', 'object_id', 'source'),)", 'object_name': 'GenericCitation'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '999'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '999'}),
            'reliability': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lexicon.Source']"})
        },
        'lexicon.language': {
            'Meta': {'ordering': "['ascii_name']", 'object_name': 'Language'},
            'ascii_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '999'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'sort_key': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'utf8_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '999'})
        },
        'lexicon.languagelist': {
            'Meta': {'ordering': "['name']", 'object_name': 'LanguageList'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_ids': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '999'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '999'})
        },
        'lexicon.lexeme': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'Lexeme'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cognate_class': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lexicon.CognateClass']", 'symmetrical': 'False', 'through': "orm['lexicon.CognateJudgement']", 'blank': 'True'}),
            'gloss': ('django.db.models.fields.CharField', [], {'max_length': '999', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lexicon.Language']"}),
            'meaning': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lexicon.Meaning']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phon_form': ('django.db.models.fields.CharField', [], {'max_length': '999', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['lexicon.Source']", 'symmetrical': 'False', 'through': "orm['lexicon.LexemeCitation']", 'blank': 'True'}),
            'source_form': ('django.db.models.fields.CharField', [], {'max_length': '999'})
        },
        'lexicon.lexemecitation': {
            'Meta': {'unique_together': "(('lexeme', 'source'),)", 'object_name': 'LexemeCitation'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '999'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lexeme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lexicon.Lexeme']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '999'}),
            'reliability': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lexicon.Source']"})
        },
        'lexicon.meaning': {
            'Meta': {'ordering': "['gloss']", 'object_name': 'Meaning'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'gloss': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'lexicon.meaninglist': {
            'Meta': {'ordering': "['name']", 'object_name': 'MeaningList'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meaning_ids': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '999'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '999'})
        },
        'lexicon.source': {
            'Meta': {'ordering': "['type_code', 'citation_text']", 'object_name': 'Source'},
            'citation_text': ('django.db.models.fields.TextField', [], {'unique': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'type_code': ('django.db.models.fields.CharField', [], {'default': "'P'", 'max_length': '1'})
        }
    }

    complete_apps = ['lexicon']
