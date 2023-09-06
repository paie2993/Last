from importlib.machinery import SourceFileLoader

SourceFileLoader("hyphenation_pattern", "/models/hyphenation_pattern.py").load_module()

__tagger = SourceFileLoader("tagger", "/models/tagger.py").load_module()

Tagger = __tagger.Tagger

SourceFileLoader("extractor", "/models/extractor.py").load_module()

__hyphenation_classifier = SourceFileLoader(
    "hyphenation_classifier", "/models/hyphenation_classifier.py"
).load_module()

HyphenedWordClassifier = __hyphenation_classifier.HyphenedWordClassifier
