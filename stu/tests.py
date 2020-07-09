from django.test import TestCase, Client

from .models import Student


class StudentTestCase(TestCase):
    def setUp(self):  # 创建一条数据用于测试
        Student.objects.create(
            name='Tony',
            sex=1,
            email='123@qq.com',
            profession='程序员',
            qq='123',
            phone='123456',
        )

    def test_create_and_sex_show(self):  # 用来测试数据创建以及sex字段的正确展示
        student = Student.objects.create(
            name='Alice',
            sex=1,
            email='234@qq.com',
            profession='程序员',
            qq='234',
            phone='234567',
        )
        self.assertEqual(student.sex_show, '男', '性别字段内容跟展示不一致！')

    def test_filter(self):  # 测试查询是否可用
        Student.objects.create(
            name='Adobe',
            sex=1,
            email='345@qq.com',
            profession='程序员',
            qq='345',
            phone='345678',
        )
        name = 'Tony',
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该只存在一个名称为{}的记录'.format(name))

    def test_get_index(self):  # 测试首页的可用性
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200, 'status code must be 200!')

    def test_post_student(self):  # 提交数据->请求首页->检查数据是否存在
        client = Client()
        data = dict(
            name='test_for_post',
            sex=1,
            email='111@qq.com',
            profession='程序员',
            qq='111',
            phone='111111',
        )
        response = client.post('/', data)
        self.assertEqual(response.status_code, 302, 'status code must be 302!')
        response = client.get('/')
        self.assertEqual(b'test_for_post' in response.content, 'response content must contain `test_for_post`')