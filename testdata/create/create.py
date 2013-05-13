#This creates a test data base populated with a few objects.
#This script should be run from pshell.

from famarc.models import DBSession, Base

from famarc.models.people import Person, Marriage
from famarc.models.places import Place
from famarc.models.tags import Tag
from famarc import upload
from famarc.models.contacts import Email, Phone

from datetime import datetime

Base.metadata.create_all()

session = DBSession()

tag_1 = Tag()
tag_1.name = "Cool"
tag_1.description = "All kinds of everything cool."

tag_2 = Tag()
tag_2.name = "Neat"
tag_2.description = "Pretty neat stuff."

tag_3 = Tag()
tag_3.name = "Nice"
tag_3.description = "You know it."


file_1_sha1 = upload.upload_file("Summer 2013 Goals.pdf",
                            open("Summer 2013 Goals.pdf").read(),
                            file_desc = "Our summer goals.")

file_2_sha1 = upload.upload_file("District.jpg",
                            open("District.jpg").read(),
                            file_desc = "The mission days.")

file_1 = session.query(File).filter(File.sha1 == file_1_sha1).one()
file_2 = session.query(File).filter(File.sha1 == file_2_sha1).one()

file_1.tags.extend([tag_1, tag_2])
file_2.tags.append(tag_1)

person_1 = Person()
person_1.given_name = "Matthew Aaron"
person_1.family_name = "Webb"
person_1.gender = "M"
person_1.birthday = datetime(1988,11,13)

email_1 = Email()
email_1.name = "Primary"
email_1.address = "we13ster@gmail.com"

email_2 = Email()
email_2.name = "University"
email_2.address = "mawebb@math.byu.edu"

person_1.emails.extend([email_1,email_2])

phone_1 = Phone()
phone_1.name = "Primary"
phone_1.number = "(385)-204-6040"

person_1.phones.append(phone_1)

person_1.files.extend([file_1, file_2])


person_2 = Person()
person_2.given_name = "Becky Louise"
person_2.family_name = "Webb"
person_2.maiden_name = "Stoker"
person_2.gender = "F"
person_2.birthday = datetime(1988,6,21)

person_2.tags.extend([tag_1, tag_2, tag_3])

person_2.files.append(file_1)

email_3 = Email()
email_3.name = "Primary"
email_3.address = "beckylouisewebb@gmail.com"

person_2.emails.append(email_3)


place_1 = Place()
place_1.name = "Washington D.C. Temple"
place_1.tags.append(tag_1)

marriage_1 = Marriage()
marriage_1.person_1 = person_1
marriage_1.person_2 = person_2
marriage_1.place = place_1

person_3 = Person()
person_3.given_name = "Charlie"
person_3.family_name = "Webb"
person_3.gender = "M/F"
person_3.mother = person_2
person_3.father = person_1
person_3.tags.append(tag_2)

session.add([person_1, person_2, person_3, tag_1, tag_2, tag_3, file_1, file_2,
             marriage_1, email_1, email_2, email_3, phone_1, place_1])
