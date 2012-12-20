# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Recipe.title'
        db.add_column('recipes_recipe', 'title',
                      self.gf('django.db.models.fields.CharField')(default='Ooops', max_length=80),
                      keep_default=False)

        # Adding field 'Recipe.slug'
        db.add_column('recipes_recipe', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='ooops', max_length=80),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Recipe.title'
        db.delete_column('recipes_recipe', 'title')

        # Deleting field 'Recipe.slug'
        db.delete_column('recipes_recipe', 'slug')


    models = {
        'recipes.food': {
            'Meta': {'object_name': 'Food'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'recipes.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'food': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Food']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measurement': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['recipes.Ingredient']", 'symmetrical': 'False'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '80'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['recipes']