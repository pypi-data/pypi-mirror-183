from src.key import Key

def test_key_with_defaults_and_seed_set():
    k = Key(seed=10)
    assert k.generated == "sbnpsagopiuzfbqpkchx"
    assert len(k.generated) == 20


def test_key_with_defaults_and_seed_set_override_length():
    k = Key(seed=10, length=10)
    assert k.generated == "sbnpsagopi"
    assert len(k.generated) == 10
