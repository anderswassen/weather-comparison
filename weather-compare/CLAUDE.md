# Weather Compare

A Next.js application for comparing weather forecasts between two Swedish locations.

## Tech Stack

- **Framework**: Next.js 16.1.6 with React 19
- **Styling**: Tailwind CSS 4
- **Testing**: Vitest + Testing Library
- **Maps**: Leaflet (dynamically imported to avoid SSR issues)
- **Weather API**: SMHI (Swedish Meteorological and Hydrological Institute)
- **Geocoding**: OpenStreetMap/Nominatim

## Key Features

- Compare weather forecasts for two Swedish locations side by side
- Interactive map showing selected locations
- Favorites system (stored in localStorage under `weather-favorites`)
- Recent locations tracking (stored in localStorage under `weather-recent`, max 5)
- Bilingual user guide (English and Swedish)
- Dark mode support

## Project Structure

```
src/
├── app/
│   └── page.tsx              # Main page component
├── components/
│   ├── LocationAutocomplete.tsx  # Location search with favorites/recent
│   ├── LocationMap.tsx           # Leaflet map (uses isolate z-0 for stacking)
│   ├── ComparisonDashboard.tsx   # Weather comparison display
│   ├── UserGuide.tsx             # Bilingual help modal
│   └── ThemeToggle.tsx           # Dark mode toggle
├── hooks/
│   ├── useWeatherComparison.ts   # Weather data fetching
│   └── useLocationStorage.ts     # Favorites/recent localStorage management
└── lib/
    └── types.ts                  # TypeScript interfaces (GeocodeResult, etc.)
```

## Commands

```bash
npm run dev        # Start development server
npm run build      # Production build
npm run test       # Run tests in watch mode
npm run test:run   # Run tests once
npm run lint       # Run ESLint
```

## Notes

- LocationMap uses `isolate z-0` CSS to create a stacking context (prevents map from overlaying modals)
- UserGuide modal uses `z-[100]` for proper layering
- LocationAutocomplete uses `role="option"` instead of nested buttons for accessibility
