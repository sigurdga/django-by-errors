# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field ingredients on 'Recipe'
        db.delete_table('recipes_recipe_ingredients')

        # Adding field 'Ingredient.recipe'
        db.add_column('recipes_ingredient', 'recipe',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['recipes.Recipe']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding M2M table for field ingredients on 'Recipe'
        db.create_table('recipes_recipe_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['recipes.recipe'], null=False)),
            ('ingredient', models.ForeignKey(orm['recipes.ingredient'], null=False))
        ))
        db.create_unique('recipes_recipe_ingredients', ['recipe_id', 'ingredient_id'])

        # Deleting field 'Ingredient.recipe'
        db.delete_column('recipes_ingredient', 'recipe_id')


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
            'measurement': ('django.db.models.fields.SmallIntegerField', [], {}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recipes.Recipe']"})
        },
        'recipes.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '80'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['recipes']