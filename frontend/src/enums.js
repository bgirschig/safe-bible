export const Filth = {
  NO_FILTH: 0,
  KEEP_EVERYTHING: 1,
  ONLY_FILTH: 2,
};

// Analytics custom variables need a unique index from 1 to 5
export const matomoCustomVariables = {
  FONT_SIZE: 1,
  DARK_MODE: 2,
  FILTH_SELECT: 3,
};

export function getEnumValueName(enumObject, value) {
  // eslint-disable-next-line no-restricted-syntax
  for (const key in enumObject) {
    if (enumObject[key] === value) return key;
  }
  return null;
}
