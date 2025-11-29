import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface UIState {
  activeTab: 'home' | 'news' | 'tasks' | 'scenarios' | 'activities';
  breakdownModalOpen: boolean;
  breakdownModalData: any | null;
}

const initialState: UIState = {
  activeTab: 'home',
  breakdownModalOpen: false,
  breakdownModalData: null,
};

const uiSlice = createSlice({
  name: 'ui',
  initialState,
  reducers: {
    setActiveTab: (state, action: PayloadAction<UIState['activeTab']>) => {
      state.activeTab = action.payload;
    },
    openBreakdownModal: (state, action: PayloadAction<any>) => {
      state.breakdownModalOpen = true;
      state.breakdownModalData = action.payload;
    },
    closeBreakdownModal: (state) => {
      state.breakdownModalOpen = false;
      state.breakdownModalData = null;
    },
  },
});

export const {
  setActiveTab,
  openBreakdownModal,
  closeBreakdownModal,
} = uiSlice.actions;

export default uiSlice.reducer;
