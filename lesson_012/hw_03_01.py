from unittest.mock import Mock

fake_1 = Mock()
print(fake_1)
print(fake_1())

print(fake_1(1, 2, 3, test=42))
print(fake_1.called)
print(fake_1(test=42))
print(fake_1.call_count)
print(fake_1.call_args)
fake_1.assert_called_with(test=42)
# fake_1.assert_called_with(test=41)
# Traceback (most recent call last):
#   File "D:\Python\Projects\UU\lessons\lesson_012\hw_03_01.py", line 12, in <module>
#     fake_1.assert_called_with(test=41)
#   File "D:\Python\Python39\lib\unittest\mock.py", line 907, in assert_called_with
#     raise AssertionError(_error_message()) from cause
# AssertionError: expected call not found.
# Expected: mock(test=41)
# Actual: mock(test=42)


fake_2 = Mock(return_value=42)
print(fake_2())

fake_3 = Mock()
print(fake_3.nonexistent_attr)
fake_3.any_attr = 27
print(fake_3.any_attr)

fake_4 = Mock(return_value=fake_3)
result = fake_4()
print(result.any_attr)
