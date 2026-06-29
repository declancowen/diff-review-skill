# Next.js Patterns

Load this pack when the affected repository or change clearly uses Next.js, especially App Router, Route Handlers, Server Components, or ISR.

## Focus areas

- Route Handler versus Server Action versus client-side fetch boundaries
- App Router layout and segment conventions
- cache invalidation and revalidation semantics
- middleware, auth gating, and edge/runtime constraints
- image, bundling, and dynamic import patterns
- SSR, ISR, RSC, and hydration tradeoffs
- parallel routes, loading states, and error boundaries

## Spec prompts

- Which layer owns data fetching and cache invalidation?
- Which components must remain server-side versus client-side?
- Which revalidation or invalidation paths can regress adjacent pages?
- Which route or layout conventions in the repo should the design preserve?
