export type NoteSummary = {
  note_id: number;
  name: string;
  created_dt: Date;
  modified_dt: Date;
};

export type Note = NoteSummary & {
  body: string;
};
