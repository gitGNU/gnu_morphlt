# morphlt is a tool for creating morphological tag databases.
#
# Copyright 2009 by Nathan Smith (nathan@nathansmith.me)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

from django.db import models

# Lemmas
class Lemma(models.Model):
    lemma = models.CharField(max_length=50)

# Words - e.g. lexical forms
class Word(model.model):
    word = models.CharField(max_length=50)
    lemma = models.ForeinKey(Lemma)

# Tokens are inflected words
# Correspond to exactly one lemma
class Token(models.Model):
    # Bind tokens to lemmas? There might be tokens which have the same form but different roots
    # e.g. "ear of corn" v. human "ear"
    # lemma = models.ForeignKey(Lemma)
    token = models.CharField(max_length=50)

class PartofSpeech(models.Model):
    part_of_speech = models.CharField(max_length=50)
    slug = models.SlugField(max_length=2)

class Person(models.Model):
    person = models.CharField(max_length=10)
    slug = models.SlugField(max_length=2)

class Number(models.Model):
    number = models.CharField(max_length=10)
    slug = models.SlugField(max_length=2)

class Gender(models.Model):
    gender = models.CharField(max_length=10)
    slug = models.SlugField(max_length=2)

class Case(models.Model):
    case = models.CharField(max_length=10)
    slug = models.SlugField(max_length=2)

class Tense(models.Model):
    tense = models.CharField(max_length=15)
    slug = models.SlugField(max_length=2)

class mood(models.Model):
    mood = models.CharField(max_length=10)
    slug = models.SlugField(max_length=2)

class Voice(models.Model):
    voice = models.CharField(max_length=10)
    slug = models.SlugField(max_length=2)

# A parsing is comprised of all of the above
class Parsing(models.Model):
    token = models.ForeignKey(Token)
    word = models.ForeignKey(Word)
    part_of_speech = models.ForeignKey(PartofSpeech)
    person = models.ForeignKey(Person)
    number = models.ForeignKey(Number)
    gender = models.ForeignKey(Gender)
    case = models.ForeignKey(Case)
    tense = models.ForeignKey(Tense)
    mood = models.ForeignKey(Mood)
    voice = models.ForeignKey(Voice)
