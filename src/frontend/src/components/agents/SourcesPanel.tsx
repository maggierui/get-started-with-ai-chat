import { ReactNode } from "react";
import { Title3, Body1, Card, Caption1, Button } from "@fluentui/react-components";
import { DocumentRegular, SaveRegular } from "@fluentui/react-icons";
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
  const handleSaveChunks = () => {
    if (sources.length === 0) return;

    // Create formatted content with ranked chunks
    const content = sources.map(source => 
      `=== Rank #${source.rank} ===\nTitle: ${source.title}\nChunk ID: ${source.chunk_id}\n\n${source.content}\n\n`
    ).join('\n');

    // Create a blob and download
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `retrieved-chunks-${new Date().toISOString().slice(0, 19).replace(/:/g, '-')}.txt`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  };

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
      <div className={styles.header}>
        <Title3 className={styles.title}>Retrieved Sources ({sources.length})</Title3>
        <Button
          appearance="primary"
          icon={<SaveRegular />}
          onClick={handleSaveChunks}
          size="small"
        >
          Save Chunks
        </Button>
      </div>
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
