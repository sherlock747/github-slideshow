const MODEL_ALIASES = {
  'gpt-5.5-thinking': 'gpt-5-thinking',
  'gpt-5-5-thinking': 'gpt-5-thinking',
  'gpt-5-thinking-latest': 'gpt-5-thinking',
  'gpt-5-thinking': 'gpt-5-thinking'
};

function mapQuotaModel(rawModel) {
  const normalizedRawModel = typeof rawModel === 'string' ? rawModel.trim() : '';
  const mappedModel = MODEL_ALIASES[normalizedRawModel] || normalizedRawModel;

  if (typeof console !== 'undefined' && typeof console.debug === 'function') {
    console.debug('[chatgpt-quota] model mapping', {
      rawModel: normalizedRawModel,
      mappedModel
    });
  }

  return mappedModel;
}

if (typeof module !== 'undefined') {
  module.exports = {
    MODEL_ALIASES,
    mapQuotaModel
  };
}
