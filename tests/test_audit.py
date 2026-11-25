import tempfile
import unittest
from pathlib import Path
from isan_validation_claim_audit.audit import audit, claims, evidence
from isan_validation_claim_audit.phrases import ISANVALIDATION, NOISANVALIDATION, GENERIC_NAMES


class AuditTests(unittest.TestCase):
    def test_phrases(self):
        self.assertEqual((len(set(ISANVALIDATION)), len(set(NOISANVALIDATION)), len(set(GENERIC_NAMES))), (50, 24, 24))
        for phrase in ISANVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase), (True, False))
        for phrase in NOISANVALIDATION:
            with self.subTest(phrase=phrase): self.assertEqual(claims(phrase), (False, True))
        self.assertEqual(claims('```\nvalidate isan\n```'), (False, False))

    def test_library_routes(self):
        for method in ('validate', 'is_valid'):
            for prefix, call in [('import stdnum.isan', 'stdnum.isan.' + method), ('import stdnum.isan as im', 'im.' + method), ('from stdnum import isan', 'isan.' + method), ('import stdnum', 'stdnum.isan.' + method), ('from stdnum.isan import ' + method, method), ('from stdnum.isan import ' + method + ' as v', 'v')]:
                with self.subTest(method=method, call=call): self.assertTrue(evidence(prefix + '\n' + call + '(x)'))

    def test_generic_routes(self):
        for name in GENERIC_NAMES:
            for source in ('obj.' + name + '(x)', 'from lib import ' + name + ' as f\nf(x)', 'obj = factory()\nobj.' + name + '(x)'):
                with self.subTest(source=source): self.assertTrue(evidence(source))

    def test_not_evidence(self):
        cases = ['import stdnum.isan', 'validate(x)', 'is_valid(x)', 'validate_isan(x)', 'obj.validate(x)', 'obj.isan(x)', 'import stdnum.isan\nstdnum.isan.compact(x)', 'import stdnum.isan\nstdnum.isan.format(x)', 'import stdnum.isan\nstdnum.isan.to_binary(x)', 'import stdnum.isan\nstdnum.isan.to_xml(x)', 'import stdnum.isan\nstdnum.isan.to_urn(x)', 'import stdnum.isan\nstdnum.isan.split(x)', 'from stdnum import ean\nean.validate(x)', 'from stdnum import ean\nean.calc_check_digit(x)', 'from stdnum import luhn\nluhn.validate(x)', 'from stdnum import luhn\nluhn.calc_check_digit(x)', 'import re\nre.match(x,y)', 'import re\nre.search(x,y)', 'import re\nre.fullmatch(x,y)', 'len(x) == 13', 'root in known', 'validators.isan(x)', 'lookup.isan(x)', '"validate isan"', 'validate_isan', 'def broken(:', 'import subprocess\nsubprocess.run(["isan-check"])', 'import stdnum.isan as im\nim = x\nim.validate(x)', 'from stdnum.isan import validate\nwith x as validate:\n validate(x)', 'def validate_isan(x): pass\nobj.validate_isan(x)']
        cases += ['from stdnum import ' + n + '\n' + n + '.validate(x)' for n in ('isbn', 'issn', 'ismn', 'grid')]
        for source in cases:
            with self.subTest(source=source): self.assertFalse(evidence(source))

    def test_findings(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d); (p/'README.md').write_text('validate isan')
            self.assertEqual(audit(p)[0]['severity'], 'HIGH')
            (p/'tests').mkdir(); (p/'tests/test_a.py').write_text('obj.validate_isan(x)')
            self.assertEqual(audit(p)[0]['severity'], 'MEDIUM')
            (p/'a.py').write_text('obj.validate_isan(x)')
            self.assertEqual(audit(p), [])
            (p/'README.md').write_text('does not validate isan')
            self.assertEqual(audit(p)[0]['severity'], 'HIGH')
            (p/'a.py').unlink(); self.assertEqual(audit(p), [])

    def test_exclusions(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d); (p/'README.md').write_text('validate isan')
            for folder in ('fixtures', 'docs', 'examples'):
                (p/folder).mkdir(); (p/folder/'a.py').write_text('obj.validate_isan(x)')
            (p/'link.py').symlink_to(p/'fixtures/a.py')
            self.assertEqual(audit(p)[0]['severity'], 'HIGH')
            (p/'src.py').write_text('obj.validate_isan(x)')
            self.assertEqual(audit(p, ['src.py'])[0]['severity'], 'HIGH')
