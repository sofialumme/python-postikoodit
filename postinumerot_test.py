from postinumerot import hae_postinumerot

def test_hae_postinumerot_korvatunturi():
    assert hae_postinumerot('KORVATUNTURI') == ['99999']

def test_hae_postinumerot_salo():
    assert hae_postinumerot('SALO') == ['24100', '24101', '24130', '24240', '24260', '24280']

def test_hae_postinumerot_tuntematon_paikka():
    assert hae_postinumerot('BLAABLAA') == None

def test_hae_postinumerot_smartpost_valilyonnit():
    assert hae_postinumerot('SMART POST') == hae_postinumerot('SMARTPOST')
