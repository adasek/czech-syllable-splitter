import pytest

from czech_syllable_splitter import split_to_syllables


@pytest.fixture
def syllable_splits() -> dict[str, list[str]]:
    return {
        "křižovala": ["kři", "žo", "va", "la"],
        "chrobák": ["chro", "bák"],
        "ahoj": ["a", "hoj"],
        "ochechule": ["o", "che", "chu", "le"],
        "a": ["a"],
        "Ch": ["Ch"],
        "CHOBOT": ["CHO", "BOT"],
        "lachtan": ["lach", "tan"],
        "plechová": ["ple", "cho", "vá"],
        "kartáček": ["kar", "tá", "ček"],
        "indulona": ["in", "du", "lo", "na"],
        "jitrnice": ["ji", "tr", "ni", "ce"],
        "pouze": ["pou", "ze"],
        "prostě": ["pro", "stě"],  # questionable
        "vráska": ["vrá", "ska"],  # questionable
        "vklad": ["vklad"],
        "vkladné": ["vklad", "né"],
        "vlnolam": ["vl", "no", "lam"],
        "podprsenka": ["pod", "pr", "sen", "ka"],
        "prvosenka": ["pr", "vo", "sen", "ka"],
        "chlívek": ["chlí", "vek"],
        "chlív": ["chlív"],
        "vlhko": ["vlh", "ko"],
        "plch": ["plch"],
        "plšík": ["pl", "šík"],
        "pláštík": ["pláš", "tík"],
        "Čtvrtek": ["Čtvr", "tek"],
        "ZMRZLINA": ["ZMRZ", "LI", "NA"],
        "jsouc": ["jsouc"],

        "prostřídat": ["pro", "stří", "dat"],
        "ustřižený": ["u", "stři", "že", "ný"],
        "horských": ["hor", "ských"],
        "sportovní": ["spor", "tov", "ní"],
        "bratrovražda": ["bra", "tro", "vraž", "da"],  # questionable
        "opatství": ["o", "pat", "ství"],
        "přístupný": ["pří", "stup", "ný"],

        "neplavkyně": ["ne", "plav", "ky", "ně"],
        "netransparentní": ["ne", "trans", "pa", "rent", "ní"],
        "nervy": ["ner", "vy"],
        "nervní": ["nerv", "ní"],

        "příklad": ["pří", "klad"],
        "připravený": ["při", "pra", "ve", "ný"],
        "příslovečný": ["pří", "slo", "več", "ný"],

        "bezelstnými": ["be", "zelst", "ný", "mi"],  # questionable
        "šestatřicetileté": ["še", "sta", "tři", "ce", "ti", "le", "té"],  # questionable
        "fajnšmekr": ["fajn", "šme", "kr"],
        "chudokrevnost": ["chu", "do", "krev", "nost"],
        "takhle": ["tak", "hle"],

        "celosvětovému": ["ce", "lo", "svě", "to", "vé", "mu"],
        "monoteistické": ["mo", "no", "te", "i", "stic", "ké"],
        "louisianské": ["lou", "i", "si", "an", "ské"]
    }
    # Keep the stem! Todo.
    #   # questionable
    #
    # "používal": ["po", "u", "ží", "val"],
    # "používat": ["po", "u", "ží", "vat"],


def test_split_to_syllables(syllable_splits):
    for word, syllables in syllable_splits.items():
        assert syllables == split_to_syllables(word), f"Syllable split for word '{word}' should be {syllables}"
