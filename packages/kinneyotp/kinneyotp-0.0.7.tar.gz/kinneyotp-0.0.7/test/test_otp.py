from kinneyotp.otp import OTP

def test_all_valid_letters_no_input():
    a = OTP()
    assert a.all_valid_letters("") == True

def test_all_valid_letters_a_letter_not_in_alphabet():
    a = OTP()
    assert a.all_valid_letters(".") == False

def test_all_valid_letters_valid_input():
    a = OTP()
    assert a.all_valid_letters("abcabc") == True

def test_encode_no_key():
    a = OTP()
    msg, val = a.encode("hello")
    assert msg != ""
    assert val == ""

def test_encode_valid_key_default_alphabet():
    a = OTP(key="hbdiq")
    msg, val = a.encode("hello")
    assert msg == ""
    assert val == "ofote"

def test_encode_letter_text_to_encode_has_letter_not_in_alphabet():
    a = OTP(alphabet="abc", key="abc")
    msg, val = a.encode("foo")
    assert msg != ""
    assert val == ""

def test_encode_letter_key_has_letter_not_in_alphabet():
    a = OTP(alphabet="abc", key="def")
    msg, val = a.encode("aaa")
    assert msg != ""
    assert val == ""

def test_decode_valid_key_default_alphabet():
    a = OTP(key="hbdiq")
    msg, val = a.decode("ofote")
    assert msg == ""
    assert val == "hello"

def test_decode_key_length_different():
    a = OTP(key="abc")
    msg, val = a.decode("a")
    assert msg != ""
    assert val == ""

def test_decode_letter_in_decode_string_not_in_alphabet():
    a = OTP(key="abc")
    msg, val = a.decode("ABC")
    assert msg != ""
    assert val == ""

def test_decode_key_has_letters_not_in_alphabet():
    a = OTP(key="ABC")
    msg, val = a.decode("abc")
    assert msg != ""
    assert val == ""

def test_with_different_alphabet():
    a = OTP(alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!", key="KFJGH")
    e = "HELLO"
    msg, val = a.encode(e)
    assert msg == ""
    assert val == "RJURV"
    msg2, val2 = a.decode(val)
    assert msg2 == ""
    assert val2 == e
