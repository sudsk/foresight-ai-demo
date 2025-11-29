import PortfolioMetrics from './PortfolioMetrics'
import SMEList from './SMEList'
import SMEDetailPanel from './SMEDetailPanel'

const HomeTab = () => {
  return (
    <div className="space-y-6">
      {/* Portfolio Metrics Cards */}
      <PortfolioMetrics />

      {/* SME List and Detail Panel */}
      <div className="grid grid-cols-12 gap-6">
        {/* SME List - Left Panel (5 columns) */}
        <div className="col-span-5">
          <SMEList />
        </div>

        {/* SME Detail Panel - Right Panel (7 columns) */}
        <div className="col-span-7">
          <SMEDetailPanel />
        </div>
      </div>
    </div>
  )
}

export default HomeTab
