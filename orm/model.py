from app import db



class Student(db.Model):
    __tablename__ = 'student'

    student_id = db.Column(db.Integer, primary_key=True)
    student_username = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(20), nullable=False)
    student_lastname = db.Column(db.String(20), nullable=False)
    student_birthday =  db.Column(db.String(20), nullable=False)
    student_group = db.Column(db.String(20), nullable=False)
    student_mail = db.Column(db.String(20), nullable=False)
    student_password = db.Column(db.String(20), nullable=False)
    student_photo = db.Column(db.String(20), nullable=False)
    student_grades = db.Column(db.String(20), nullable=False)
    student_proglanguage = db.Column(db.String(20), nullable=False)
    student_specialization = db.Column(db.String(20), nullable=False)
    # User_User_Group = db.relationship("Group", secondary='user_group')


class Teacher(db.Model):
    __tablename__ = 'teacher'

    teacher_id = db.Column(db.Integer, primary_key=True)
    teacher_username = db.Column(db.Integer, primary_key=True)
    teacher_name = db.Column(db.String(20), nullable=False)
    teacher_lastname = db.Column(db.String(20), nullable=False)
    teacher_birthday = db.Column(db.String(20), nullable=False)
    teacher_position = db.Column(db.String(20), nullable=False)
    teacher_subject = db.Column(db.String(20), nullable=False)
    teacher_mail = db.Column(db.String(20), nullable=False)
    teacher_password = db.Column(db.String(20), nullable=False)
    teacher_photo = db.Column(db.String(20), nullable=False)
    teacher_hobby = db.Column(db.String(20), nullable=False)
    teacher_proglanguage = db.Column(db.String(20), nullable=False)
    teacher_item = db.Column(db.String(20), nullable=False)
    teacher_works = db.Column(db.String(20), nullable=False)
    teacher_specialization = db.Column(db.String(20), nullable=False)
    # Group_User_Group = db.relationship("User", secondary='user_group')
    # Group_Group_Post = db.relationship("Post", secondary='group_post')


#
# class User_Group(db.Model):
#     __tablename__ = 'user_group'
#
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
#     group_id = db.Column(db.Integer, db.ForeignKey('group.group_id'), primary_key=True)
#

class Post(db.Model):
    __tablename__ = 'post'

    post_id = db.Column(db.Integer, primary_key=True)
    post_content = db.Column(db.String(1000), nullable=False)
    post_hashtag = db.Column(db.String(20), nullable=False)

    Post_Group_Post = db.relationship("Group", secondary='group_post')
    notification = db.relationship("Notification")




class Group_Post(db.Model):
    __tablename__ = 'group_post'

    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.group_id'), primary_key=True)


class Notification(db.Model):
    __tablename__ = 'notification'

    notification_id = db.Column(db.Integer, primary_key=True)
    notification_time = db.Column(db.String(5), primary_key=True)
    notification_text = db.Column(db.String(100), primary_key=True)

    post_id = db.Column(db.Integer, db.ForeignKey("post.post_id"))


