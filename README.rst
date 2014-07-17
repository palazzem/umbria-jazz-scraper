===================
Umbria jazz scraper
===================

Simple scraper used as example in a Computer Science course of University of Perugia.
This scraper will export `Umbria Jazz program`_ into a JSON format using `Scrapy`_.

.. _Umbria Jazz program: http://www.umbriajazz.com/pagine/programma-umbria-jazz
.. _Scrapy: http://scrapy.readthedocs.org/en/0.24/

Requirements
------------

Create a Python ``virtualenv`` and install all requirements:

.. code-block:: bash

    $ pip install -r requirements.txt

This project set Scrapy to version ``0.24``.

Usage
-----

Run this command to export all concerts into a JSON format:

.. code-block:: bash

    $ scrapy crawl jazz -o concerts.json
