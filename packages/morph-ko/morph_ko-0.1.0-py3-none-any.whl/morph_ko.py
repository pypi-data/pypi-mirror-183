from unicodedata import normalize

CONSONENT_ENDING_PARTICLES = {
  '이', '은', '을', '에', '에서', '으로'
}

VOWEL_ENDING_PARTICLES = {
  '가', '는', '를', '에', '에서', '로'
}

# source: https://github.com/JDongian/python-jamo/blob/master/jamo/jamo.py
JAMO_VOWELS_MODERN = [chr(_) for _ in range(0x1161, 0x1176)]


def morph_noun(noun, consonent_ending_particles=CONSONENT_ENDING_PARTICLES, vowel_ending_particles=VOWEL_ENDING_PARTICLES):
  """
  Apply particles to a noun depending on whether it ends in a consonent
  """
  particles = VOWEL_ENDING_PARTICLES if ends_in_vowel(noun) else CONSONENT_ENDING_PARTICLES

  return {noun + particle for particle in particles}


def ends_in_vowel(word):
  """
  Does the word end in a vowel sound
  """
  # TODO: validation
  chars = normalize('NFD', word)
  return chars[-1] in JAMO_VOWELS_MODERN
