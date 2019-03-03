from Learning_Journal.models import Journal_Entry
from datetime import datetime
from Learning_Journal import db
db.create_all()

a = Journal_Entry("python", datetime.utcnow(), 12, "jdksacs", "wacsdcws", 1)

c = Journal_Entry("dsfa", datetime.utcnow(), 12, "jdksacs", "wacsdcws", 1)


db.session.add_all([a,c])
db.session.commit()
b = Journal_Entry.query.all()



print(b)