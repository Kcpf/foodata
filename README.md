Foodata

A Python wrapper around the IFood API.

Introduction
============

This library provides a pure Python interface for the IFood API. It was tested with Python 3.

`IFood <http://ifood.com.br>`_ provides a service that allows people to order food from restaurants in their app. IFood exposes a web services API, that was found during a network analysis on their website and this library is intended to make it easier for all people to access these provided data.

Getting the code
================

The code is hosted at https://github.com/Kcpf/foodata

Check out the latest development version anonymously with:

    $ git clone git@github.com:Kcpf/foodata.git
    $ cd foodata

To install dependencies, run:

    $ pip install -r requirements.txt

Running Tests
=============
To run the unit tests with a single Python version:

    $ python -m unittest discover

Documentation
=============
TODO

Using
=====

The library provides a Python wrapper around the IFood API and the IFood data model. To get started, check out the examples in the examples/ folder.

Also, you will need to get authentication from their website (see .env.example). The easiest way, that I found until now, is to get the authentication from requests sent when using their services. 

Models
=====

The library utilizes models to represent various data structures returned by IFood. Those models are:
    * foodata.classes.Category
    * foodata.classes.Merchant
    * foodata.classes.Item
    * foodata.classes.Facet
    * foodata.classes.Choice
    * foodata.classes.Garnish

API
=====

The API is exposed via the ``foodata.api`` package.

You will need to get authentication from their website (see .env.example). The easiest way, that I have found until now, is to get the authentication from requests sent when using their services. 

Todo
=====

Patches, pull requests, and bug reports are `welcome <https://github.com/Kcpf/foodata/issues/new>`_, just please keep the style consistent with the original source.

In particular, having more example scripts would be a huge help. Also, creating an useful documentation.

Contributors
=====

It's a full-on open source project. So, if you want to colaborate, feel free to fork our repository and send a PR. 
