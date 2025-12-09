import { ReactNode } from "react";
import { Title3, Body1, Card, Caption1 } from "@fluentui/react-components";
import { DocumentRegular } from "@fluentui/react-icons";
import styles from "./SourcesPanel.module.css";

export interface ISource {
  rank: number;
  title: string;
  chunk_id: string;
  content: string;
}

interface ISourcesPanelProps {
  sources: ISource[];
}

export function SourcesPanel({ sources }: ISourcesPanelProps): ReactNode {
  if (sources.length === 0) {
    return (
      <div className={styles.sourcesPanel}>
        <Title3 className={styles.title}>Retrieved Sources</Title3>
        <Caption1 className={styles.emptyState}>
          No sources retrieved yet. Ask a question to see relevant documents.
        </Caption1>
      </div>
    );
  }

  return (
    <div className={styles.sourcesPanel}>
      <Title3 className={styles.title}>Retrieved Sources ({sources.length})</Title3>
      <div className={styles.sourcesList}>
        {sources.map((source, index) => (
          <Card key={index} className={styles.sourceCard}>
            <div className={styles.sourceHeader}>
              <DocumentRegular className={styles.icon} />
              <div className={styles.sourceRank}>#{source.rank}</div>
            </div>
            <Body1 className={styles.sourceTitle}>{source.title}</Body1>
            {source.chunk_id && (
              <Caption1 className={styles.chunkId}>Chunk: {source.chunk_id}</Caption1>
            )}
            <Caption1 className={styles.sourceContent}>{source.content}</Caption1>
          </Card>
        ))}
      </div>
    </div>
  );
}
