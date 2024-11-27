# تحويل النص إلى Bytes
b = bytes("hello", "utf-8")  # تحويل النص "hello" إلى Bytes
print(b)  # الناتج: b'hello'

# تحويل النص إلى ByteArray
ba = bytearray("hello", "utf-8")  # تحويل النص "hello" إلى ByteArray
print(ba)  # الناتج: bytearray(b'hello')

# إنشاء memoryview من ByteArray
mv = memoryview(bytearray("hello", "utf-8"))  # إنشاء memoryview من bytearray
print(mv)  # الناتج: <memory at 0x...>

# التحويل من قائمة من الأزواج إلى قاموس
pairs = [("name", "Alice"), ("age", 25), ("city", "New York")]
dct = dict(pairs)
print(dct)  # الناتج: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# تحويل Bytes إلى نص
txt = "Hello"
b = bytes(txt, 'utf-8')
print(b)  # الناتج: b'Hello'

# تحويل Bytes إلى نص
b = b'Hello'
txt = b.decode('utf-8')
print(txt)  # الناتج: Hello

# التحويل من قائمة إلى frozenset
lst = [1, 2, 3, 4]
frozen = frozenset(lst)
print(frozen)  # الناتج: frozenset({1, 2, 3, 4})

# التحويل من عدد صحيح إلى النظام الثنائي
num = 10
binary = bin(num)
print(binary)  # الناتج: '0b1010'

# التحويل من عدد صحيح إلى النظام الست عشري
num = 255
hex_num = hex(num)
print(hex_num)  # الناتج: '0xff'

# التحويل من عدد صحيح إلى النظام الثماني
num = 8
octal = oct(num)
print(octal)  # الناتج: '0o10'
