# useRender.ts

**Path**: `apps\front-ecommerce\app\composables\useRender.ts`

## Summary
In development mode, assignment render property works fine
but in production SFC overwrites it with an empty function
because no &lt;template&gt; section defined.

Filthy hack to avoid this in production.
https://github.com/vuejs/core/issues/4980

## Interfaces
- `Arrayable`

## Function Details

### `useRender`

- **Parameters**: `render: (`

