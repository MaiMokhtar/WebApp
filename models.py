from exts import db


class Num(db.Model):
    """class Num:
        id:int primary key
        no:int
    """
    id = db.Column(db.Integer(), primary_key=True)
    no = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f"<Num {self.no} >"

    def save(self):
        """
        The save function is used to save the changes made to a model instance.
        It takes in no arguments and returns nothing.

        :param self: Refer to the current instance of the class
        :return: The object that was just saved
        :doc-author:jod35
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        The delete function is used to delete a specific row in the database. It takes no parameters and returns nothing.

        :param self: Refer to the current instance of the class, and is used to access variables that belongs to the class
        :return: Nothing
        :doc-author:jod35
        """
        db.session.delete(self)
        db.session.commit()

    def update(self, no):
        """
        The update function updates the title and description of a given blog post.
        It takes two parameters, title and description.

        :param self: Access variables that belongs to the class.
        :param no: Update the number of the post.
        :return: A dictionary with the updated value of number.
        :doc-author:jod35
        """
        self.no = no
        db.session.commit()


# user model
class User(db.Model):
    """Class User:
        id:integer
        username:string
        email:string
        password:string
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        """
        returns string rep of object

        """
        return f"<User {self.username}>"

    def save(self):
        db.session.add(self)
        db.session.commit()
