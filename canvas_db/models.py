from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship

from .orm import get_base


Base = get_base()


class Course(Base):
    """
    Модель "Курс"
    """

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    sis_source_id = Column(String(255))

    def __repr__(self):
        return '<Course {} (id={}, sis_source_id={})>'.format(self, self.id, self.sis_source_id)
    
    def __str__(self):
        return self.name


class CourseSection(Base):
    """
    Модель "Секция курса"
    """

    __tablename__ = 'course_sections'

    id = Column(Integer, primary_key=True)
    sis_source_id = Column(String(255))
    course_id = Column(ForeignKey('courses.id'))
    course = relationship('Course')
    name = Column(String(255))
    workflow_state = Column(String(255))

    def __repr__(self):
        return '<CourseSection {} (id={}, sis_source_id={})>'.format(self, self.id, self.sis_source_id)
    
    def __str__(self):
        return self.name