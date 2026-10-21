import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://janmensik.github.io',
  base: '/rodokmen',
  trailingSlash: 'always',
  build: { format: 'directory' },
});
