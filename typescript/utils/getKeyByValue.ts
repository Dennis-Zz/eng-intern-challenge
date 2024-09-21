export default function getKeyByValue<T>(obj: object, value: T): string | undefined {
  return Object.entries(obj).find(([key, val]) => val === value)?.[0];
}

