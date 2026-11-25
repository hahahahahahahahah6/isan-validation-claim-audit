# International Standard Audiovisual Number claim audit

This offline static audit compares documented audiovisual-number capability claims with Python call patterns. It scans the root README and Markdown files under docs, excluding fenced code; inline code counts. It never executes source or accesses the network.

Install and run:

```
isan-validation-claim-audit audit .
python3 -m isan_validation_claim_audit audit . --json
```

Use `--ignore PREFIX` repeatedly to omit paths, `--fail-on medium` to include test-only findings, and `--verbose` for additional context. The default threshold is high. Exit status is 0 for a pass, 2 for a finding at or above the threshold, and 1 for a usage or I/O error. Use `--version` for the version.

The finding identifiers are:

```
documented-isan-validation-claim-false
documented-no-isan-validation-claim-false
```

A positive claim without production evidence is high severity, or medium when evidence occurs only in tests. A denial with production evidence is high severity. A positive claim without any source files is high severity; a denial without source passes.

The recognized library calls are:

```
from stdnum import isan
isan.validate(value)
isan.is_valid(value)
```

Generic named calls are also recognized when imported or used as attributes. Imports and aliases are resolved within one module; local definitions and rebinding can shadow imports. Test files count separately, while fixtures, examples, documentation, symlinks and invalid syntax do not provide production evidence.

## Differentiation

This audit does not cover generic input checking.
This audit does not cover ISBN.
This audit does not cover ISSN.
This audit does not cover IBAN.
This audit does not cover UUID.
This audit does not cover semantic version.
This audit does not cover hardware address.
This audit does not cover BIC.
This audit does not cover cron-expression validation.
This audit does not cover cron-expression description.
This audit does not cover scheduled execution.
This audit does not cover date validation.
This audit does not cover timeout.
This audit does not cover payment processing.
This audit does not cover credit-card extraction.
This audit does not cover authentication with a one-time code or confirmation link.
This audit does not cover password verification for authentication.
This audit does not cover password hashing.
This audit does not cover password generation.
This audit does not cover PDF encryption.
This audit does not cover email.
This audit does not cover SMS.
This audit does not cover document extraction.
This audit does not cover barcode decoding.
This audit does not cover email validation.
This audit does not cover phone-number validation.
This audit does not cover password strength.
This audit does not cover JSON-schema validation.
This audit does not cover credit-card validation.
This audit does not cover domain validation.
This audit does not cover URL validation.
This audit does not cover IP-address validation.
This audit does not cover JSON decoding.
This audit does not cover regex matching.
This audit does not cover URL parsing.
This audit does not cover web fetching.
This audit does not cover DNS resolution.
This audit does not cover barcode generation.
This audit does not cover account-number extraction.
This audit does not cover vehicle-number extraction.
This audit does not cover vehicle-number decoding.
This audit does not cover vehicle history lookup.
This audit does not cover hex-color validation.
This audit does not cover ORCID.
This audit does not cover ISNI.
This audit does not cover DOI.
This audit does not cover CUSIP.
This audit does not cover SEDOL.
This audit does not cover ISIN.
This audit does not cover security record lookup.
This audit does not cover securities identifier extraction.
This audit does not cover IMEI.
This audit does not cover MEID.
This audit does not cover ESN.
This audit does not cover ISMN.
This audit does not cover GRid.
This audit does not cover EAN.
This audit does not cover serial-number validation.
This audit does not cover registry lookup.
This audit does not cover audiovisual-number extraction.
This audit does not cover spreadsheet reading.
This audit does not cover spreadsheet generation.
This audit does not cover word-document reading.
This audit does not cover word-document generation.
This audit does not cover presentation reading.
This audit does not cover presentation generation.
This audit does not cover PDF extraction.
This audit does not cover PDF generation.
This audit does not cover PDF merging.
This audit does not cover PDF splitting.
This audit does not cover PDF rotation.
This audit does not cover PDF form filling.
This audit does not cover PDF watermarking.
This audit does not cover PDF redaction.
This audit does not cover PDF compression.
This audit does not cover PDF annotation.
This audit does not cover table extraction.
This audit does not cover OCR.
This audit does not cover document extraction.
This audit does not cover e-signature.
This audit does not cover screen recording.
This audit does not cover video generation.
This audit does not cover QR code generation.
This audit does not cover barcode scanning.
This audit does not cover audio mixing.
This audit does not cover audio generation.
This audit does not cover audio editing.
This audit does not cover source separation.
This audit does not cover speech recognition.
This audit does not cover text to speech.
This audit does not cover noise suppression.
This audit does not cover music generation.
This audit does not cover music transcription.

## Limitations

```
validate isan
```

The bare phrase above can describe a manual runbook step rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
isan validation
```

The bare phrase above can describe a roadmap feature rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
isan validator
```

The bare phrase above can describe a hosted page rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
isan check
```

The bare phrase above can describe a field-presence lint rule rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
check isan
```

The bare phrase above can describe a manual runbook step rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
verify isan
```

The bare phrase above can describe visual confirmation of a title and cut rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
isan code validation
```

The bare phrase above can describe a field-presence check rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
valid isan
```

The bare phrase above can describe an example value rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
isan is valid
```

The bare phrase above can describe example output rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
isan is invalid
```

The bare phrase above can describe example error text rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
isan validity
```

The bare phrase above can describe a configuration flag or column name rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
isan format validation
```

The bare phrase above can describe a format description rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
validate isan number
```

The bare phrase above can describe a hexadecimal shape check without a check-character judgment rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
isan number validation
```

The bare phrase above can describe a specification section without code rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
validate isan code
```

The bare phrase above can describe a manual runbook step rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
check isan code
```

The bare phrase above can describe a manual runbook step rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
validate isan16
```

The bare phrase above can describe a manual runbook step rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
isan24 validation
```

The bare phrase above can describe a specification section without code rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
isan number check
```

The bare phrase above can describe a cataloguing checklist item rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
isan validation
```

The bare phrase above can describe an external service result rather than an implemented capability, so it can produce a false positive requiring human judgment.

```
isan
```

The bare phrase above is not recognized because it does not establish the specific capability.

```
isan number
```

The bare phrase above is not recognized because it does not establish the specific capability.

```
validate identifier
```

The bare phrase above is not recognized because it does not establish the specific capability.

```
check character
```

The bare phrase above is not recognized because it does not establish the specific capability.

```
iso 7064
```

The bare phrase above is not recognized because it does not establish the specific capability.

```
root
```

The bare phrase above is not recognized because it does not establish the specific capability.

```
episode
```

The bare phrase above is not recognized because it does not establish the specific capability.

A compact call only strips separators and upper-cases, so it is not evidence.

A split call only splits the number into root, episode, and version parts, so it is not evidence.

A format call only reformats the number, so it is not evidence.

A to_binary call only encodes the number as bytes, so it is not evidence.

A to_xml call only renders the number as XML, so it is not evidence.

A to_urn call only formats the number as a URN, so it is not evidence.

A bare EAN check has no audiovisual-number leg: the latter is hexadecimal with ISO 7064 Mod 37, 36 check characters, not a 13-digit decimal number.

A bare Luhn check has no audiovisual-number leg.

The check characters are optional in the library: a 16- or 24-character form without them passes on length and format alone.

The library does not check whether the root identifies a registered work.

ISBN checks are not evidence.

ISSN checks are not evidence.

ISMN checks are not evidence.

GRid checks are not evidence.

A registry lookup is not evidence.

A length check alone is not evidence.

A root-element membership check alone is not evidence.

A regular expression match alone is not evidence.

A generic validate method on an unknown base may be missed.

A bare import is not evidence.

A roadmap, changelog or TODO in scanned prose still counts as a claim.

A denial outside the listed phrases may be missed.

A document outside the root README and docs directories is not scanned.

Evidence split across modules is missed.

A local definition shadows the corresponding route name.

Dead code counts as evidence.

A subprocess invocation is not evidence.

Alias chains that cannot be resolved are missed.

Matching is static and exact, not semantic.

A generic input check alone is not evidence of an audiovisual-number judgment.

An email check alone is not evidence of an audiovisual-number judgment.

A phone check alone is not evidence of an audiovisual-number judgment.

A URL check alone is not evidence of an audiovisual-number judgment.

An IP address check alone is not evidence of an audiovisual-number judgment.

A domain check alone is not evidence of an audiovisual-number judgment.

An ISBN check alone is not evidence of an audiovisual-number judgment.

An ISSN check alone is not evidence of an audiovisual-number judgment.

An IBAN check alone is not evidence of an audiovisual-number judgment.

An ISIN check alone is not evidence of an audiovisual-number judgment.

An IMEI check alone is not evidence of an audiovisual-number judgment.

An MEID check alone is not evidence of an audiovisual-number judgment.

A GRid check alone is not evidence of an audiovisual-number judgment.

An EAN check alone is not evidence of an audiovisual-number judgment.
