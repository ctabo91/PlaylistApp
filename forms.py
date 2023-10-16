"""Forms for playlist app."""

from wtforms import SelectField, StringField, TextAreaField
from wtforms.validators import InputRequired, Length, Optional
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Name', validators=[InputRequired(message='Can not leave blank'), Length(max=50)])

    description = TextAreaField('Description', validators=[Optional(), Length(max=150)])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Title', validators=[InputRequired(message='Can not leave blank'), Length(max=50)])

    artist = StringField('Artist', validators=[InputRequired(message='Can not leave blank'), Length(max=50)])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
