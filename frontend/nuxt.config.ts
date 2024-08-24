// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: "2024-04-03",

  devtools: {
    enabled: true,

    timeline: {
      enabled: true,
    },
  },

  ssr: true,

  typescript: {
    typeCheck: true
  },

  dir: {
    assets: "src/assets",
    app: "src/app",
    layouts: "src/layouts",
    middleware: "src/middleware",
    modules: "src/modules",
    pages: "src/pages",
    plugins: "src/plugins",
    public: "src/public",
  },

  modules: ["@nuxt/eslint"]
});