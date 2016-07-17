# Mezzanine Polls

Mezzanine-style implementation of the Django polls (from the tutorial).

## How to play

1. Clone the repo

1. Check out the initial commit

1. Install the requirements: `pip install -r requirements.txt` (this will
   install Mezzanine and all Python dependencies).

1. Inside `polldemo/` copy and rename `local_settings.py.sample` to
   `local_settings.py` (further instructions in the file).

1. Initialize the database: `python manage.py createdb`. Take note of the
   username and password you use (those will be the admin credentials). You can
   answer all other prompts with the defaults.

1. Start the Django development server `python manage.py runserver`. Visit
   http://localhost:8000/polls to view the site. The admin is at
   http://localhost:8000/admin.

1. Replay the commits as you walk through the slides. You can re-type
   everything or just look at the diffs, they are very small and clear.
   Remember to run migrations!
