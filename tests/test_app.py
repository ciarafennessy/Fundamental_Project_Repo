from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Recipes, Ingredients, Instructions

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        testentry1 = Recipes(recipe_name="test recipe", recipe_time="test time", servings=10)
        testentry2 = Ingredients(ingredient_name_quantity="test ingredient", recipe_id=1)
        testentry3 = Instructions(step="test step", instruction="test instruction", recipe_id=1)
        db.session.add(testentry1)
        db.session.add(testentry2)
        db.session.add(testentry3)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    
class TestViews1(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)

class TestViews2(TestBase):
    def test_getrecipes(self):
        response = self.client.get(url_for('recipes'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Recipes', response.data)

class TestViews3(TestBase):
    def test_getaddrecipe(self):
        response = self.client.get(url_for('add_recipe'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add a Recipe', response.data)

class TestViews4(TestBase):
    def test_getaddingredients(self):
        response = self.client.get(url_for('add_i'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add Ingredients', response.data)

class TestViews5(TestBase):
    def test_getaddinstructions(self):
        response = self.client.get(url_for('add_inst'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add Instructions', response.data)

class TestViews6(TestBase):
    def test_getrecipe(self):
        response = self.client.get(url_for('recipe', rid=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ingredients:', response.data)

class TestAddr(TestBase):
    def test_add_r(self):
        response = self.client.post(
            url_for('add_recipe'),
            data = dict(recipe_name="test recipe", recipe_time="test time", servings=10),
            follow_redirects=True
        )
        self.assertIn(b'Add a Recipe', response.data)

class TestAddi(TestBase):
    def test_add_i(self):
        response = self.client.post(
            url_for('add_i'),
            data = dict(i_name="test ingredient", recipe=2),
            follow_redirects=True
        )
        self.assertIn(b'Add Ingredients', response.data)

class TestAddinst(TestBase):
    def test_add_inst(self):
        response = self.client.post(
            url_for('add_inst'),
            data = dict(step="test step", instruction="test instruction", recipe=2),
            follow_redirects=True
        )
        self.assertIn(b'Add Instructions', response.data)


class TestUpInst(TestBase):
    def test_up_inst(self):
        response = self.client.post(
            url_for('update_inst', instid=1),
            data = dict(inst_step="updated step", inst="updated instruction"),
            follow_redirects=True
        )
        self.assertIn(b'Instructions', response.data)


class TestDelr(TestBase):
    def test_del_r(self):
        response = self.client.get(url_for('delete_recipe', rid = 1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'test recipe', response.data)

class TestrewriteI(TestBase):
    def test_rewrite_i(self):
        response = self.client.get(url_for('rewrite_ing', rid=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        self.assertIn(b'Add Ingredients', response.data)

class TestChooser(TestBase):
    def test_choose_r(self):
        response = self.client.post(
            url_for('select_recipe'),
            data = dict(recipe_id=1),
            follow_redirects=True
        )
        self.assertIn(b'Ingredients:', response.data)
        
