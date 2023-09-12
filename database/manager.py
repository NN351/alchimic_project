from .models import StudentGroup, Student


class StudentGroupManager():
    def __init__(self, session):
        self.session = session
        self.model = StudentGroup

    def insert_group(self, data):
        group = StudentGroup(
            name = data['name']
        )
        self.session.add(group)
        self.session.commit()

    def get_all_groups(self):
        groups = self.session.query(self.model).all()
        return groups

    
    def search_by_group_name(self, search_name):
        result=self.session.query(self.model).filter(
            self.model.name.contains(search_name)
            )
        return result

