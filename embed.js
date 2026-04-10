/* Agentic Economy Definition Embed Widget v1.0
 * Usage:
 *   <div class="ae-embed" data-id="A1" data-theme="dark"></div>
 *   <script src="https://agenticeconomy.dev/embed.js"></script>
 */

(function() {
  'use strict';

  const DEFINITIONS = {
    A1: { cat: "A", source: "Microsoft Research", sub: "Rothschild, Mobius, Hofman et al.", date: "May 2025", def: "Assistant agents act on behalf of consumers and service agents represent businesses, interacting programmatically to facilitate transactions.", notes: "arXiv:2505.15799. The most cited academic definition." },
    A2: { cat: "A", source: "Stripe / OpenAI", sub: "Agentic Commerce Protocol (ACP)", date: "Sep 2025", def: "Checkout flows where an AI agent discovers a product for a human and pays via Stripe's Shared Payment Token.", notes: "agenticcommerce.dev. Deployed in ChatGPT as \"Instant Checkout\"." },
    A3: { cat: "A", source: "Google / Shopify / Walmart", sub: "Universal Commerce Protocol (UCP)", date: "Jan 2026", def: "Full commerce lifecycle -- discovery, comparison, checkout, post-purchase -- with the agent navigating the journey for the human.", notes: "A checkout state machine extending human e-commerce to agentic surfaces." },
    A4: { cat: "A", source: "Google / Mastercard / PayPal", sub: "AP2", date: "2025", def: "OAuth-based payments allowing agents to purchase on behalf of their human owners using saved payment methods.", notes: "Payment: Mastercard/PayPal/fiat. Identity: OAuth." },
    A5: { cat: "A", source: "Visa", sub: "\"Agentic Ready\" program", date: "Mar 2026", def: "Agent-initiated payments via tokenization and biometric verification, tied back to human cardholders.", notes: "Biometric auth ensures a human is behind every transaction." },
    A6: { cat: "A", source: "Mastercard", sub: "\"Agent Pay\"", date: "Dec 2025", def: "Agentic Tokens with spend limits set by the human, issued to AI agents via passkeys.", notes: "The agent has a budget, not a bank account." },
    A7: { cat: "A", source: "McKinsey", sub: "\"The End of Inertia\"", date: "Aug 2025", def: "Agents break the \"consumer inertia dividend\" with real-time micro-auctions for best rates.", notes: "Projects agent-mediated commerce at $3-5T by 2030." },
    A8: { cat: "A", source: "IBM", sub: "\"What Is Agentic Commerce?\"", date: "Jan 2026", def: "AI agents act on behalf of consumers or businesses to research, negotiate and complete purchases.", notes: "ibm.com/think. Straightforward Category A framing." },
    A9: { cat: "A", source: "Salesforce", sub: "", date: "2025-2026", def: "AI agents embedded in CRM workflows to assist human buyers and sellers through existing sales processes.", notes: "Enterprise-facing. The agent optimizes the sales funnel." },
    A10: { cat: "A", source: "JPMorgan", sub: "", date: "2025-2026", def: "AI agents assisting financial advisors and clients with product discovery and transaction execution.", notes: "Financial services context. Payment: traditional fiat." },
    A11: { cat: "A", source: "Nosto", sub: "", date: "2025-2026", def: "AI-powered personalization agents for e-commerce, optimizing product recommendations and checkout for human shoppers.", notes: "The agent is a conversion optimization tool." },
    A12: { cat: "A", source: "Deloitte", sub: "commerce context", date: "2025", def: "AI agents acting on our behalf -- shopping, negotiating, executing purchases.", notes: "Distinguished from Deloitte's enterprise/workforce framing." },
    A13: { cat: "A", source: "Stripe / Tempo", sub: "Machine Payment Protocol (MPP)", date: "Mar 2026", def: "Agents need to transact with businesses and one another -- M2M payments on Visa/Stripe rails, fiat + stablecoins.", notes: "Hybrid A/C. Built on human financial infrastructure." },
    A14: { cat: "A", source: "Jason Cochran", sub: "\"Own the Workflow, Not the App\"", date: "Feb 2026", def: "Intents become interfaces, agents become default delegates, workflows become the product.", notes: "Hybrid A/B. Workflows, not transactions, are the unit of value." },
    B1: { cat: "B", source: "Gartner", sub: "", date: "2025-2026", def: "100 million agents by 2028. 33% of enterprise apps will include agentic AI. 15% of day-to-day business decisions made autonomously. $18T in economic activity influenced.", notes: "The optimism and the skepticism come from the same analyst house." },
    B2: { cat: "B", source: "Sequoia Capital", sub: "Bob McGrew, ex-OpenAI CTO", date: "May 2025", def: "Agents will be commoditized and priced at compute costs due to near-infinite supply. Services shift from selling tools to selling results.", notes: "The SaaS seat model dies. Outcome-based pricing replaces it." },
    B3: { cat: "B", source: "Sequoia Capital", sub: "Konstantine Buhler", date: "May 2025", def: "An agent economy is one in which agents don't just communicate information -- they transfer resources, make transactions, keep track of each other, understand trust and reliability, and actually have their own economy.", notes: "Hybrid B/C. Three challenges: persistent identity, seamless protocols, security/trust." },
    B4: { cat: "B", source: "Deloitte", sub: "\"Agentic Enterprise\"", date: "2025", def: "Agents as autonomous partners inside organizations, making multi-step decisions without human approval at each step.", notes: "Here the agent is an employee, not a shopper." },
    B5: { cat: "B", source: "Capgemini / OECD", sub: "", date: "2025", def: "1.7x ROI on AI operations. 21% of organizations running multi-agent systems.", notes: "Agents optimize existing processes, not create new markets." },
    B6: { cat: "B", source: "Vilnius University", sub: "", date: "Mar 2026", def: "Agents divide responsibilities, coordinate tasks, cross-check each other's work inside enterprise workflows.", notes: "Academic treatment of multi-agent coordination." },
    B7: { cat: "B", source: "Pascal Bornet et al.", sub: "\"Self-Running Businesses\"", date: "World Scientific, 2025", def: "AI as entrepreneur -- businesses that operate with minimal human involvement.", notes: "Pushes Category B toward its logical extreme." },
    B8: { cat: "B", source: "NotoriousPLG", sub: "\"Year of the Agentic Workforce\"", date: "Feb 2025", def: "Vertical-specific agents as workers -- legal, medical, compliance. Outcome-based pricing per vertical.", notes: "The agent is a specialist, not a generalist." },
    C1: { cat: "Ccr", source: "Fetch.ai / ASI Alliance", sub: "", date: "2021-2025", def: "\"Machine Economy\" -- agents negotiate, trade, and deliver services using FET/ASI tokens with self-custodial wallets.", notes: "The earliest mover. Active since 2021." },
    C2: { cat: "Ccr", source: "Olas (Valory)", sub: "", date: "2021-2025", def: "Agent economies where agents hire and sell services to each other, governed by on-chain DAO mechanisms.", notes: "Payment: crypto/tokens. Identity: on-chain wallets." },
    C3: { cat: "Ccr", source: "Coinbase / Cloudflare", sub: "x402", date: "May 2025", def: "HTTP 402 status code + stablecoin micropayments. Account-less, subscription-free, pay-per-use.", notes: "Settlement in <500ms. Payment: USDC." },
    C4: { cat: "Ccr", source: "Circle", sub: "Nanopayments testnet", date: "Mar 2026", def: "Gas-free USDC transfers down to $0.000001. Off-chain aggregation, batched on-chain settlement.", notes: "Eliminates gas fees by batching." },
    C5: { cat: "Ccr", source: "Kite", sub: "", date: "2026", def: "EVM-compatible Layer 1 specifically for agentic payments. \"Know Your Agent\" (KYA) framework with hierarchical on-chain identity.", notes: "Payment: stablecoin, zero-gas. Identity: KYA." },
    C6: { cat: "Ccr", source: "Gate Ventures", sub: "", date: "Dec 2025", def: "Four-layer Machine Economy framework: infrastructure, identity, economic, governance. Settlement via crypto/x402.", notes: "A VC framework, not a protocol." },
    C7: { cat: "Ccr", source: "Ken Huang & Lisa Tan", sub: "\"The AI Agent Economy\"", date: "Springer, Feb 2025", def: "Token economies incentivizing agent behavior. Virtuals, AI16z, and Token-of-Things as examples. Decentralized governance.", notes: "Academic treatment of crypto-native agent economics." },
    C8: { cat: "Ccr", source: "Xu et al.", sub: "\"The Agent Economy: A Blockchain-Based Foundation\"", date: "arXiv, Feb 2026", def: "Five-layer architecture: physical infrastructure (DePIN), identity (W3C DIDs), cognition (RAG + MCP), economic settlement (account abstraction), collective governance (DAOs).", notes: "The most architecturally complete proposal in Category C." },
    C9: { cat: "Ccr", source: "Nevermined", sub: "", date: "2026", def: "\"Agentic Process Automation\" -- autonomous businesses with DID-based identity and crypto/fiat settlement.", notes: "Hybrid crypto/fiat but blockchain-first." },
    C10: { cat: "Ccr", source: "Bosch / IOTA / BearingPoint", sub: "", date: "2018-2025", def: "\"Machine Economy\" via IoT + distributed ledger technology. The historical precursor -- machines paying machines for data and services.", notes: "Predates the LLM wave by years." },
    C11: { cat: "Ccr", source: "OKX", sub: "OnchainOS", date: "2026", def: "Natural language commands routed to DeFi across 60+ chains. MCP integration for agent-to-DeFi interaction.", notes: "The agent speaks natural language; the infrastructure translates." },
    C12: { cat: "Cs", source: "BotNode / VMP-1.0", sub: "Dechamps Otamendi", date: "Mar 2026", def: "Agents with own currency ($TCK), escrow-backed settlement, quantitative reputation (CRI 0-100), and automated dispute resolution. No blockchain.", notes: "The only non-crypto entry in Category C." },
    D1: { cat: "D", source: "World Economic Forum", sub: "\"Trust Is the New Currency\"", date: "Jul 2025", def: "Three trust domains: human-to-human, human-to-agent, agent-to-agent. Trust is the fundamental constraint, not compute.", notes: "Shapes the regulatory conversation." },
    D2: { cat: "D", source: "Bank of International Settlements", sub: "BIS", date: "2026", def: "\"Agentic Finance\" -- the Agentic Financial Market Model (AFMM). Four-layer architecture: perception, reasoning, strategy, execution.", notes: "Warns of algorithmic herding, automated bank runs, flash crashes." },
    D3: { cat: "D", source: "a16z Crypto / YC / Medium", sub: "sovereign framing", date: "2025-2026", def: "Agents as sovereign actors. AI-native banks. Agents that own assets, sign contracts, and execute trades independently.", notes: "Influential in shaping narrative." },
    D4: { cat: "D", source: "Macroeconomic consensus", sub: "\"doom loop\"", date: "2026", def: "If Category B agents replace enough workers, wages collapse, consumer demand collapses. If demand collapses, the businesses that agents transact with have nothing to sell.", notes: "Convergent concern across multiple economic analyses." },
    D5: { cat: "D", source: "Antler VC", sub: "\"Unleashing the Autonomous Economy\"", date: "Jan 2026", def: "Frames the agent economy through Crossmint, Olas, and on-chain rails. Mentions ACK-ID, Nevermined ID.", notes: "VC analysis that straddles building and analyzing." },
    D6: { cat: "D", source: "Argoz Consultants", sub: "\"The Rise of the Machine Economy\"", date: "Mar 2026", def: "Machines negotiate, trade, and transact without human oversight.", notes: "Consultancy framing." },
    D7: { cat: "D", source: "MIT Technology Review EmTech", sub: "\"The Dawn of the Agent Economy\"", date: "Nov 2025", def: "Trillions of AI agents as buyers, sellers, collaborators. NANDA building the \"DNS of the agentic web.\"", notes: "Visionary framing." },
    E1: { cat: "E", source: "Google", sub: "Agent-to-Agent Protocol (A2A)", date: "Apr 2025", def: "Agent discovery and communication. Agents publish Agent Cards at /.well-known/agent.json, exchange tasks via JSON-RPC over HTTPS.", notes: "v0.3. 150+ partners." },
    E2: { cat: "E", source: "Anthropic", sub: "Model Context Protocol (MCP)", date: "2024", def: "A standard for LLMs to discover and invoke external tools. Focused on tool interoperability.", notes: "modelcontextprotocol.io." },
    E3: { cat: "E", source: "Trulioo / Worldpay / Skyfire", sub: "KYA Infrastructure", date: "2026", def: "\"Digital Agent Passport\" -- Know Your Agent identity verification for autonomous agents.", notes: "The KYC equivalent for machines." },
    E4: { cat: "E", source: "IEEE 7012", sub: "", date: "Draft, 2026", def: "Standard for terms and agreements between autonomous entities.", notes: "The first formal standards body to address agent-to-agent contracts." },
    E5: { cat: "E", source: "Forrester / Exista.io", sub: "Agent Discovery Optimization (ADO)", date: "2025-2026", def: "SEO is for humans. ADO is for agents. A brand invisible to agents is invisible to the agentic economy.", notes: "New concept." },
    E6: { cat: "E", source: "IETF", sub: "Verified Commerce for Agent Protocols (VCAP)", date: "Internet-Draft, 2026", def: "Cryptographic proof of work delivery for agent commerce. IETF standardization track.", notes: "Hybrid C/E." },
    E7: { cat: "E", source: "OECD", sub: "\"Agentic AI: Landscape and Conceptual Foundations\"", date: "2026", def: "Working paper on terminology and regulatory framing for agentic AI systems.", notes: "Hybrid D/E. Shapes regulatory vocabulary." },
    E8: { cat: "E", source: "a16z", sub: "Keycard investment", date: "Oct 2025", def: "The identity layer for the agent economy. Finding: non-human identities outnumber human employees 96-to-1 in finance.", notes: "Finance already has more machine identities than human ones." },
    E9: { cat: "E", source: "Urbach et al.", sub: "\"Conceptualizing the Machine Economy\"", date: "PACIS 2021", def: "The complete integration and participation of economically autonomous acting machines in economic processes.", notes: "The earliest academic paper. Predates the protocol wave." },
    E10: { cat: "E", source: "Goenka et al.", sub: "TessPay", date: "arXiv, Jan 2026", def: "Verify-then-Pay Infrastructure for Trusted Agentic Commerce. Escrow + TEE/TLS verification.", notes: "Hybrid C/E. Proves the seller delivered what the buyer paid for." }
  };

  const COLORS = {
    A: '#3b82f6',
    B: '#a78bfa',
    Ccr: '#f59e0b',
    Cs: '#34d399',
    D: '#f87171',
    E: '#22d3ee'
  };

  function getCSSForTheme(theme) {
    if (theme === 'light') {
      return `
        .ae-embed-card {
          background: #ffffff;
          color: #1f2937;
          border: 1px solid #e5e7eb;
        }
        .ae-embed-cat-dot {
          background: var(--ae-cat-color);
        }
        .ae-embed-source {
          color: #6b7280;
        }
        .ae-embed-def {
          color: #374151;
        }
        .ae-embed-footer {
          color: #9ca3af;
          border-top-color: #f3f4f6;
        }
        .ae-embed-link {
          color: var(--ae-cat-color);
        }
        .ae-embed-link:hover {
          opacity: 0.8;
        }
      `;
    }
    // dark theme (default)
    return `
      .ae-embed-card {
        background: #141a38;
        color: #e8ecf4;
        border: 1px solid #1a2348;
      }
      .ae-embed-cat-dot {
        background: var(--ae-cat-color);
      }
      .ae-embed-source {
        color: #a0a9c0;
      }
      .ae-embed-def {
        color: #d1d5db;
      }
      .ae-embed-footer {
        color: #8e99b8;
        border-top-color: #1a2348;
      }
      .ae-embed-link {
        color: var(--ae-cat-color);
      }
      .ae-embed-link:hover {
        opacity: 0.8;
      }
    `;
  }

  function createCard(id, def, theme) {
    const catColor = COLORS[def.cat] || '#34d399';

    const card = document.createElement('div');
    card.className = 'ae-embed-card';
    card.style.cssText = `
      --ae-cat-color: ${catColor};
      max-width: 400px;
      border-radius: 8px;
      padding: 16px;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      font-size: 14px;
      line-height: 1.6;
    `;

    const header = document.createElement('div');
    header.style.cssText = `
      display: flex;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 12px;
    `;

    const dot = document.createElement('div');
    dot.className = 'ae-embed-cat-dot';
    dot.style.cssText = `
      width: 8px;
      height: 8px;
      border-radius: 50%;
      margin-top: 3px;
      flex-shrink: 0;
    `;

    const headerText = document.createElement('div');
    headerText.style.cssText = 'flex: 1; min-width: 0;';

    const catLabel = document.createElement('div');
    catLabel.style.cssText = `
      font-weight: 600;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 2px;
      color: var(--ae-cat-color);
    `;
    catLabel.textContent = `Category ${def.cat}`;

    const source = document.createElement('div');
    source.className = 'ae-embed-source';
    source.style.cssText = 'font-size: 12px; margin-bottom: 4px;';
    source.textContent = def.source;

    const sub = document.createElement('div');
    sub.style.cssText = `
      font-size: 12px;
      font-weight: 500;
      margin-bottom: 2px;
    `;
    sub.textContent = def.sub;

    const date = document.createElement('div');
    date.style.cssText = `
      font-size: 11px;
      color: #a0a9c0;
      opacity: 0.7;
    `;
    date.textContent = def.date;

    headerText.appendChild(catLabel);
    headerText.appendChild(source);
    if (def.sub) headerText.appendChild(sub);
    headerText.appendChild(date);

    header.appendChild(dot);
    header.appendChild(headerText);

    const definition = document.createElement('p');
    definition.className = 'ae-embed-def';
    definition.style.cssText = `
      margin: 12px 0;
      font-size: 14px;
      line-height: 1.6;
    `;
    definition.textContent = def.def;

    const footer = document.createElement('div');
    footer.className = 'ae-embed-footer';
    footer.style.cssText = `
      padding-top: 12px;
      border-top: 1px solid;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      color: #8e99b8;
    `;

    const idLabel = document.createElement('span');
    idLabel.textContent = 'Definition ' + id;

    const link = document.createElement('a');
    link.className = 'ae-embed-link';
    link.href = 'https://agenticeconomy.dev/agentic-economy-definitions.html#' + id;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    link.style.cssText = `
      text-decoration: none;
      font-weight: 500;
      cursor: pointer;
    `;
    link.textContent = 'Read more';

    footer.appendChild(idLabel);
    footer.appendChild(link);

    card.appendChild(header);
    card.appendChild(definition);
    card.appendChild(footer);

    return card;
  }

  function init() {
    // Inject CSS
    const style = document.createElement('style');

    let css = `
      .ae-embed-card {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }
      .ae-embed-card * {
        box-sizing: border-box;
      }
    `;

    // Collect all themes
    const themesNeeded = new Set();
    document.querySelectorAll('.ae-embed').forEach(el => {
      const theme = el.getAttribute('data-theme') || 'dark';
      themesNeeded.add(theme);
    });

    // Add CSS for each theme
    themesNeeded.forEach(theme => {
      css += getCSSForTheme(theme);
    });

    style.textContent = css;
    document.head.appendChild(style);

    // Render embeds
    document.querySelectorAll('.ae-embed').forEach(el => {
      const id = el.getAttribute('data-id');
      const theme = el.getAttribute('data-theme') || 'dark';

      if (!id) {
        console.warn('ae-embed element missing data-id attribute');
        return;
      }

      const def = DEFINITIONS[id];
      if (!def) {
        console.warn('Definition not found for ID:', id);
        return;
      }

      const card = createCard(id, def, theme);
      el.appendChild(card);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
