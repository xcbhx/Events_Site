"""Create database models to represent tables."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy import Enum
from events_app import db  


# Many-to-Many Association Table
guest_event_table = db.Table(
    'guest_event',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'), primary_key=True)
)

# class EventType(enum.Enum):
#     Party = 'Party'
#     Study = 'Study'
#     Networking = 'Networking'

class Guest(db.Model):
    __tablename__ = 'guest'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80))
    events_attending = db.relationship('Event', secondary=guest_event_table,back_populates='guests')

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    date_and_time = db.Column(db.DateTime)
    # event_type = db.Column(Enum(EventType))
    guests = db.relationship('Guest', secondary=guest_event_table, back_populates='events_attending')