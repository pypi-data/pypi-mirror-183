Scora Notify
=============================
This package implements a Slack notification abstraction to be used in various projects.

This packages uses logging for console outputs.

Development
-----------------------------


Build, install, test locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    # build from this source -- considering that dependencies are resolved
    rm -rf ./dist/* && python3 -m build

    # From another venv -- install 
    virtualenv -p python3
    . ./venv/bin/activate
    pip install <REPO_HOME>/dist/scora-notify-0.1.0.tar.gz 


    # Import and run
    from scora_notify import Notify 
    notify=Notify(slack_token="", slack_channel="", step="", tenant="", project="")

