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

type RetrievalMode = "natural" | "metadata_inference";

interface ISourcesPanelProps {
  sources: ISource[];
  question: string;
  mode?: RetrievalMode;
  indexName?: string;
  semanticConfig?: string;
  indexDescription?: string;
  metadataInferenceEnabled?: boolean;
}

export function SourcesPanel({
  sources,
  question,
  mode = "natural",
  indexName,
  semanticConfig,
  indexDescription,
  metadataInferenceEnabled,
}: ISourcesPanelProps): ReactNode {
  const handleSaveChunks = () => {
    if (sources.length === 0) return;

    const metadataInferenceOn = (metadataInferenceEnabled !== undefined)
      ? metadataInferenceEnabled
      : mode === "metadata_inference";

    // Create filename from first 5-6 words of question
    const words = question.trim().split(/\s+/).slice(0, 6);
    const cleanWords = words.map(w => w.replace(/[^a-zA-Z0-9]/g, '')).filter(w => w.length > 0);
    const timestamp = new Date().toISOString().slice(0, 19).replace(/:/g, '-');
    const filename = cleanWords.length > 0 
      ? `${cleanWords.join('-')}-${timestamp}.txt`
      : `retrieved-chunks-${timestamp}.txt`;

    // Create formatted content with question and ranked chunks
    const header = `Question: ${question}\nMode: ${mode}\nMetadata inference: ${metadataInferenceOn ? 'on' : 'off'}\nIndex: ${indexName || 'Unknown'}\nSemantic config: ${semanticConfig || 'None'}\nIndex description: ${indexDescription || 'None'}\nTimestamp: ${timestamp}\n${'='.repeat(80)}\n\n`;
    const chunksContent = sources.map(source => 
      `=== Rank #${source.rank} ===\nTitle: ${source.title}\nChunk ID: ${source.chunk_id}\n\n${source.content}\n\n`
    ).join('\n');
    const content = header + chunksContent;

    // Create a blob and download
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
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
        <div className={styles.headerText}>
          <Title3 className={styles.title}>Retrieved Sources ({sources.length})</Title3>
          <Caption1 className={styles.mode}>Mode: {mode === "metadata_inference" ? "Metadata inference" : "Natural"}</Caption1>
        </div>
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
