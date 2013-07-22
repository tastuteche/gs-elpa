#!/usr/bin/env python

from distutils.core import setup

setup(name          = 'g-sorcery',
      version       = '0.1_alpha',
      description   = 'g-sorcery framework for automated ebuild generators',
      author        = 'Jauhien Piatlicki',
      author_email  = 'piatlicki@gmail.com',
      packages      = ['g_sorcery', 'gs_elpa', 'gs_ctan'],
      package_data  = {'gs_elpa': ['data/*'],
                       'gs_ctan': ['data/*']},
      scripts       = ['bin/g-sorcery', 'bin/gs-elpa', 'bin/gs-ctan'],
      data_files    = [('/etc/g-sorcery/', ['gs-elpa.json']),
                       ('/etc/g-sorcery/', ['gs-ctan.json']),
                       ('/etc/g-sorcery/', ['g-sorcery.cfg']),
                       ('/etc/layman/overlays/', ['gs-elpa-overlays.xml']),
                       ('/etc/layman/overlays/', ['gs-ctan-overlays.xml'])],
      license       = 'GPL',
      )
