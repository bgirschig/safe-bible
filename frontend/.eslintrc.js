module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    'plugin:vue/essential',
    '@vue/airbnb',
  ],
  parserOptions: {
    parser: 'babel-eslint',
  },
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'no-else-return': 'off',
    'prefer-destructuring': 'off',
    'import/prefer-default-export': 'off',
    'prefer-const': ['error', {
      destructuring: 'all',
    }],
    'no-underscore-dangle': 'off',
  },
};
