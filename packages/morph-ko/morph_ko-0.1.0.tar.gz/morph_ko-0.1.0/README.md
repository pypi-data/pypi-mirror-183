# Morph

Utility for generating variations of Korean words.

This is intended to be used for matching words as they appear in the dictionary to tokens in text (어절).
For example, the sentence "우리는 오늘 동해로 간다" contains

- "우리는" which is a combination of "우리" plus the particle "는"
- "동해로" which is a combination of "동해" plus the particle "로"

## Install
- `pip install morph_po`

## Usage

- morph_noun() generates variations of nouns with particles applied based on whether the noun ends in a vowel or a consonent

## See also

- [KoParadigm](https://github.com/Kyubyong/KoParadigm) generates inflected forms of verbs
