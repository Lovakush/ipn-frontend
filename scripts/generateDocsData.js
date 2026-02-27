/**
 * Script to parse SUMMARY.md and generate documentation.json
 * ES Module version
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

// Get __dirname equivalent in ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Configuration
const SUMMARY_PATH = path.join(__dirname, '../SUMMARY.md');
const OUTPUT_PATH = path.join(__dirname, '../src/data/documentation.json');

// For development/testing, allow override via command line
const summaryPath = process.argv[2] || SUMMARY_PATH;

function categorizeByRepo(repo) {
  if (repo === 'backend') return 'backend';
  if (repo === 'frontend') return 'frontend';
  return 'other';
}

function parseMarkdownLink(line) {
  // Match: [DisplayName](filename.md) <!-- repo:backend -->
  // Uses lazy .+? so filenames containing ] like [[sitemap].xml.ts] are handled correctly
  const match = line.match(/\[(.+?)\]\(([^)]+)\)/);
  if (!match) return null;

  const [, displayName, mdFileName] = match;

  // Extract repo from HTML comment appended by rebuild_summary
  const repoMatch = line.match(/<!--\s*repo:(\w+)\s*-->/);
  const repo = repoMatch ? repoMatch[1] : null;

  // Extract original file from .md filename
  const withoutMd = mdFileName.replace('.md', '');
  const parts = withoutMd.split('_');
  const fullPath = parts.join('/');

  return {
    displayName,
    fileName: displayName,
    mdFile: mdFileName,
    path: fullPath,
    repo: repo || '',
    category: categorizeByRepo(repo || '')
  };
}

function parseSummary(content) {
  const lines = content.split('\n');
  const structure = {
    categories: {},
    files: [],
    stats: {
      total: 0,
      backend: 0,
      frontend: 0,
      other: 0
    }
  };
  
  let currentSection = null;
  let currentSubsection = null;
  const indentStack = [];
  
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    
    // Skip empty lines and main title
    if (!line || line === '# Documentation Index') continue;
    
    // Section headers (## Controllers, ## Services, etc.)
    if (line.startsWith('## ')) {
      currentSection = line.replace('##', '').trim();
      if (!structure.categories[currentSection]) {
        structure.categories[currentSection] = {
          name: currentSection,
          subsections: {},
          fileCount: 0
        };
      }
      continue;
    }
    
    // Parse nested structure
    const indent = lines[i].match(/^ */)[0].length;
    
    // Bold subsection (**Api**, **Controller**, etc.)
    if (line.startsWith('**') && line.endsWith('**')) {
      const subsectionName = line.replace(/\*\*/g, '');
      
      if (!currentSection) continue;
      
      // Determine nesting level
      const nestingPath = [...indentStack.filter((_, idx) => {
        const lineIndent = lines.findIndex((l, li) => li < i && l.includes(indentStack[idx]));
        return lineIndent !== -1;
      }), subsectionName];
      
      const pathKey = nestingPath.join(' > ');
      
      if (!structure.categories[currentSection].subsections[pathKey]) {
        structure.categories[currentSection].subsections[pathKey] = {
          name: subsectionName,
          path: nestingPath,
          files: []
        };
      }
      
      currentSubsection = pathKey;
      continue;
    }
    
    // File links
    if (line.includes('[') && line.includes('](')) {
      const fileData = parseMarkdownLink(line);
      if (!fileData) continue;
      
      // Add metadata
      fileData.id = structure.files.length;
      fileData.section = currentSection || 'Uncategorized';
      fileData.subsection = currentSubsection || '';
      
      // Add to files array
      structure.files.push(fileData);
      
      // Add to category
      if (currentSection && structure.categories[currentSection]) {
        structure.categories[currentSection].fileCount++;
        
        if (currentSubsection && structure.categories[currentSection].subsections[currentSubsection]) {
          structure.categories[currentSection].subsections[currentSubsection].files.push(fileData.id);
        }
      }
      
      // Update stats
      structure.stats.total++;
      structure.stats[fileData.category]++;
    }
  }
  
  return structure;
}

function generateSearchIndex(structure) {
  return structure.files.map(file => ({
    id: file.id,
    text: `${file.displayName} ${file.fileName} ${file.path} ${file.section} ${file.subsection}`.toLowerCase(),
    category: file.category
  }));
}

async function main() {
  try {
    console.log('🚀 Starting documentation generation...\n');
    
    // Read SUMMARY.md
    console.log(`📖 Reading SUMMARY.md from: ${summaryPath}...`);
    const summaryContent = fs.readFileSync(summaryPath, 'utf-8');
    
    // Parse the content
    console.log('🔍 Parsing documentation structure...');
    const structure = parseSummary(summaryContent);
    
    // Generate search index
    console.log('🔎 Generating search index...');
    const searchIndex = generateSearchIndex(structure);
    
    // Create output
    const output = {
      ...structure,
      searchIndex,
      generatedAt: new Date().toISOString()
    };
    
    // Ensure output directory exists
    const outputDir = path.dirname(OUTPUT_PATH);
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }
    
    // Write to file
    console.log('💾 Writing documentation.json...');
    fs.writeFileSync(OUTPUT_PATH, JSON.stringify(output, null, 2));
    
    // Also copy to public folder for runtime access
    const publicOutputPath = path.join(__dirname, '../public/data/documentation.json');
    const publicOutputDir = path.dirname(publicOutputPath);
    if (!fs.existsSync(publicOutputDir)) {
      fs.mkdirSync(publicOutputDir, { recursive: true });
    }
    fs.writeFileSync(publicOutputPath, JSON.stringify(output, null, 2));
    
    // Print statistics
    console.log('\n✅ Documentation generated successfully!\n');
    console.log('📊 Statistics:');
    console.log(`   Total files: ${structure.stats.total}`);
    console.log(`   Backend (PHP): ${structure.stats.backend}`);
    console.log(`   Frontend (JS/JSON): ${structure.stats.frontend}`);
    console.log(`   Other: ${structure.stats.other}`);
    console.log(`   Categories: ${Object.keys(structure.categories).length}`);
    console.log(`\n📁 Output: ${OUTPUT_PATH}`);
    console.log(`📁 Public: ${publicOutputPath}`);
    
  } catch (error) {
    console.error('❌ Error generating documentation:', error);
    process.exit(1);
  }
}

// Run the script
main();