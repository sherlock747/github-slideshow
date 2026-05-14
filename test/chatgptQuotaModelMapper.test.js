const assert = require('assert');
const { mapQuotaModel } = require('../src/chatgptQuotaModelMapper');

const thinkingAliases = [
  'gpt-5.5-thinking',
  'gpt-5-5-thinking',
  'gpt-5-thinking-latest',
  'gpt-5-thinking'
];

for (const model of thinkingAliases) {
  assert.strictEqual(mapQuotaModel(model), 'gpt-5-thinking');
}

assert.strictEqual(mapQuotaModel('gpt-5'), 'gpt-5');
assert.strictEqual(mapQuotaModel(' gpt-5.5-thinking '), 'gpt-5-thinking');

console.log('chatgptQuotaModelMapper tests passed');
