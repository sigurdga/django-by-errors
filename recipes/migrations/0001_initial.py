# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Food'
        db.create_table('recipes_food', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('recipes', ['Food'])

        # Adding model 'Ingredient'
        db.create_table('recipes_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('food', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recipes.Food'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('measurement', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal('recipes', ['Ingredient'])

        # Adding model 'Recipe'
        db.create_table('recipes_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('recipes', ['Recipe'])

        # Adding M2M table for field ingredients on 'Recipe'
        db.create_table('recipes_recipe_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['recipes.recipe'], null=False)),
            ('ingredient', models.ForeignKey(orm['recipes.ingredient'], null=False))
        ))
        db.create_unique('recipes_recipe_ingredients', ['recipe_id', 'ingredient_id'])


    def backwards(self, orm):
        # Deleting model 'Food'
        db.delete_table('recipes_food')

        # Deleting model 'Ingredient'
        db.delete_table('recipes_ingredient')

        # Deleting model 'Recipe'
        db.delete_table('recipes_recipe')

        # Removing M2M table for field ingredients on 'Recipe'
        db.delete_table('recipes_recipe_ingredients')


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
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['recipes']