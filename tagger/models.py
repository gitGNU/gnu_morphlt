# morphlt is a tool for creating morphological tag databases.
#
# Copyright 2009 by Nathan Smith (nathan@ndansmith.net) <http://ndansmith.net/>
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

# Need a database of lemmas
class Lemma(models.Model):
    lemma = models.CharField(max_length=50)

# Words are inflected lemmas
# Correspond to exactly one lemma
class Word(models.Model):
    # Bind words to lemmas? There might be words which have the same form but different roots
    # e.g. "ear of corn" v. human "ear"
    # lemma = models.ForeignKey(Lemma)
    word = models.CharField(max_length=50)

class PartofSpeech(models.Model):
    part_of_speech = models.CharField(max_length=50)
    slug = models.CharField(max_length=2)

# A parsing is comprised of
# - the word
# - the lemma (or root)
# - part of speech
# - etc.
# TODO: Finish the parsing schema
class Parsing(models.Model):
    word = models.ForeignKey(Word)
    lemma = models.ForeignKey(Lemma)
    part_of_speech = models.ForeignKey(PartofSpeech)

